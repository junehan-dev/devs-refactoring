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


def render_plain_text(data):
	ret = f"state detail(Username: {data['customer']})\n";
	for perf in data["performances"]:
		ret += f" {perf['play']['name']}: {itousd(perf['amount'])}$ {perf['audience']}audiences\n";

	ret += f"total_amount: {itousd(data['total_amount'])}$\n";
	ret += f"Accumulated points: {data['total_volume_credits']}points\n";
	return (ret);


def render_html(data):
	from functools import reduce

	ret = f"<h1>statement Detail {data['customer']}</h1>\n";
	ret += "<table>\n";
	ret += "<tr><th>Play</th><th>Seats</th><th>price</th></tr>\n";
	ret += reduce(
		lambda a, perf: a + f"""<tr>
		<td>{perf['play']['name']}</td>
		<td>{perf['audience']}seats</td>
		<td>{itousd(perf['amount'])}</td>
		</tr>\n""",
		(perf for perf in data["performances"]), ""
	);
	ret += f"</table>\n";
	ret += f"<p>total: <em>{itousd(data['total_amount'])}</em></p>\n";
	ret += f"<p>points: <em>{itousd(data['total_volume_credits'])}</em></p>\n";
	return (ret);
		

if __name__ == "__main__":
	import json
	from statements import statement

	with open("./resources/invoices.json", 'r') as f:
		invoices = json.loads(f.read());

	for invoice in invoices:
		print(render_plain_text(statement(invoice)));
	for invoice in invoices:
		print(render_html(statement(invoice)));



	exit(0);

