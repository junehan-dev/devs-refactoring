from amounts import amount_for

_plays = None;


def statement(invoice):
	total_amount = 0;
	volume_credits = 0;
	ret = f"state detail(Username: {invoice['customer']})\n";

	for perf in invoice["performances"]:
		this_amount = amount_for(perf, play_for(perf));
		volume_credits += max((perf["audience"] - 30, 0));
		if (play_for(perf) == "comedy"):
			volume_credits += int(perf["audience"] / 5);

		ret += f" {play_for(perf)['name']}: {int(this_amount/100)} {perf['audience']}audiences\n";
		total_amount += this_amount;

	ret += f"Accumulated points: {volume_credits}points\n";
	return (ret)


def play_for(aPerformance):
	return (_plays[aPerformance["playID"]])


if __name__ == "__main__":
	import json

	with open("./resources/invoices.json", 'r') as f:
		invoices = json.loads(f.read());

	with open("./resources/plays.json", 'r') as f:
		_plays = json.loads(f.read());

	for invoice in invoices:
		print(statement(invoice));

	exit(0);

