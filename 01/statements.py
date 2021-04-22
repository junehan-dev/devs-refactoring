from performances import PerformanceCalculator
from functools import reduce

_plays = None;


def get_volume_credit(perf):
	result = max((perf.audience - 30, 0));
	if (perf.play["type"] == "comedy"):
		result += int(perf.audience / 5);
	return (result);


def get_total_volume_credits(perfs):
	return reduce(lambda p, perf: p + get_volume_credit(perf), perfs, 0);


def get_total_amount(perfs):
	return sum((perf.amount for perf in perfs));


def play_for(aPerformance):
	return (_plays[aPerformance["playID"]]);


def enrich_perf(perf):
	result = PerformanceCalculator(perf, play_for(perf));
	return (result);


def statement(invoice):
	global _plays;
	if (not _plays):
		import json
		with open("./resources/plays.json", 'r') as f:
			_plays = json.loads(f.read());

	context_data = {};
	context_data["customer"] = invoice["customer"];
	context_data["performances"] = [enrich_perf(perf) for perf in invoice["performances"]];
	context_data["total_amount"] = get_total_amount(context_data["performances"]);
	context_data['total_volume_credits'] = get_total_volume_credits(context_data['performances']);
	return (context_data);

