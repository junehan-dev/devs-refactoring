from amounts import amount_for

def statement(invoice, plays):
	total_amount = 0;
	volume_credits = 0;
	ret = f"state detail(Username: {invoice['customer']})\n";

	for perf in invoice["performances"]:
		play = plays[perf["playID"]];
		this_amount = amount_for(perf, play);
		volume_credits += max((perf["audience"] - 30, 0));

		if (play["type"] == "comedy"):
			volume_credits += int(perf["audience"] / 5);

		ret += f" {play['name']}: {int(this_amount/100)} {perf['audience']}audiences\n";
	ret += f"Accumulated points: {volume_credits}points\n";
	return (ret)

if __name__ == "__main__":
	import json

	with open("./resources/invoices.json", 'r') as f:
		invoices = json.loads(f.read());
	with open("./resources/plays.json", 'r') as f:
		plays = json.loads(f.read());

	for invoice in invoices:
		print(statement(invoice, plays));
	exit(0);

