def distance(p1, p2):
	p1_sum = sum(p1);
	p2_sum = sum(p2);
	return (p1_sum - p2_sum if (p1_sum > p2_sum) else p2_sum - p1_sum);

def radiance(degrees):
	pass

def calculate_time():
	return (600);


def track_summary(points):
	def calculate_distance():
		result = 0;
		point_len = len(points);
		i = 1;
		while (i < point_len):
			result += distance(points[i - 1], points[i]);
			i += 1;
		return (result);


	total_time = calculate_time();
	total_distance = calculate_distance();
	pace = (total_time / 60 / total_distance);
	return ({
		"time": total_time,
		"distance": total_distance,
		"pace": pace,
	});


if __name__ == "__main__":
	points_data = [
		(33, 44), (55, 33),
		(66, 45), (45, 33),
	]
	ret = track_summary(points_data);
	print(ret);

