from amounts import amount_for
from functools import reduce

_plays = None;

def get_volume_credit(perf):
	result = max((perf["audience"] - 30, 0));
	if (perf["play"]["type"] == "comedy"):
		result += int(perf["audience"] / 5);
	return (result);


def get_total_volume_credits(perfs):
	return reduce(lambda p, perf: p + get_volume_credit(perf), perfs, 0);


def get_total_amount(perfs):
	return sum((perf['amount'] for perf in perfs));


def play_for(aPerformance):
	return (_plays[aPerformance["playID"]]);


def statement(invoice):
	global _plays;
	if (not _plays):
		import json
		with open("./resources/plays.json", 'r') as f:
			_plays = json.loads(f.read());

	context_data = {};
	context_data["customer"] = invoice["customer"];
	set_perfs = lambda el: ((el.update({"play":play_for(el)}) or el.update({"amount":amount_for(el)})) or el);
	context_data["performances"] = [perf for perf in map(set_perfs, invoice["performances"])];
	context_data["total_amount"] = get_total_amount(context_data["performances"]);
	context_data['total_volume_credits'] = get_total_volume_credits(context_data['performances']);
	return (context_data);

