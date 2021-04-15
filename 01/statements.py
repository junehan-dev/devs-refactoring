from amounts import amount_for

_plays = None;


def statement(invoice):
	total_amount = 0;
	volume_credits = 0;
	ret = f"state detail(Username: {invoice['customer']})\n";

	for perf in invoice["performances"]:
		this_amount = amount_for(perf, play_for(perf));
		ret += f" {play_for(perf)['name']}: {itousd(this_amount)}$ {perf['audience']}audiences\n";
		total_amount += this_amount;

	for perf in invoice["performances"]:
		volume_credits += max((perf["audience"] - 30, 0));
		if (play_for(perf) == "comedy"):
			volume_credits += int(perf["audience"] / 5);

	ret += f"total_amount: {itousd(total_amount)}$\n";
	ret += f"Accumulated points: {volume_credits}points\n";
	return (ret);


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

