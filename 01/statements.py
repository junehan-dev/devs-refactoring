from amounts import amount_for

_plays = None;

def get_volume_credit(perf):
	result = max((perf["audience"] - 30, 0));
	if (perf["play"]["type"] == "comedy"):
		result += int(perf["audience"] / 5);
	return (result);


def get_total_volume_credits(perfs):
	result = 0;
	for perf in perfs:
		result += get_volume_credit(perf);
	return (result);


def render_plain_text(data):
	ret = f"state detail(Username: {data['customer']})\n";
	for perf in data["performances"]:
		ret += f" {perf['play']['name']}: {itousd(perf['amount'])}$ {perf['audience']}audiences\n";

	ret += f"total_amount: {itousd(data['total_amount'])}$\n";
	ret += f"Accumulated points: {data['total_volume_credits']}points\n";
	return (ret);


def statement(invoice):
	context_data = {};
	context_data["customer"] = invoice["customer"];
	set_perfs = lambda el: ((el.update({"play":play_for(el)}) or el.update({"amount":amount_for(el)})) or el);
	context_data["performances"] = [perf for perf in map(set_perfs, invoice["performances"])];
	context_data["total_amount"] = sum((perf['amount'] for perf in context_data['performances']));
	context_data['total_volume_credits'] = get_total_volume_credits(context_data['performances']);
	return render_plain_text(context_data);


def play_for(aPerformance):
	return (_plays[aPerformance["playID"]]);


def itousd(amount):
	amount /= 100;
	src = f"{int(amount)}";
	src_len = len(src);
	if (src_len < 4):
		return (src);

	offset = src_len % 3;
	max_i = (src_len // 3) + 1 if offset else (src_len // 3);
	dest = [None] * (max_i);
	i = 0;
	if (offset):
		dest[0] = src[0:offset] + ',';
		i += 1;

	while (i < max_i - 1):
		dest[i] = src[offset:offset + 3] + ',';
		i += 1;
		offset += 3;

	dest[i] = src[offset:];
	return ("".join(dest));


if __name__ == "__main__":
	import json

	with open("./resources/invoices.json", 'r') as f:
		invoices = json.loads(f.read());

	with open("./resources/plays.json", 'r') as f:
		_plays = json.loads(f.read());

	for invoice in invoices:
		print(statement(invoice));

	exit(0);

