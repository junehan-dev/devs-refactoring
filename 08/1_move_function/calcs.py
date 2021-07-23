import math

def calculate_time():
	return (600);

def get_total_distance(points):
	def distance(p1, p2):
		_EARTH_RADIUS = 3959;
		dLat = radiance(p2[0]) - radiance(p1[0]);
		dLon = radiance(p2[-1]) - radiance(p1[-1]);
		a = (math.pow(math.sin(dLat / 2), 2)
			+ math.cos(radiance(p2[0]))
			* math.cos(radiance(p1[0]))
			* math.pow(math.sin(dLon / 2), 2)
		);
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));
		return (_EARTH_RADIUS * c);

	def radiance(degrees):
		return (degrees * math.pi / 180);

	print("called global");
	result = 0;
	point_len = len(points);
	i = 1;
	while (i < point_len):
		result += distance(points[i - 1], points[i]);
		i += 1;
	return (result);

def track_summary(points):
	total_time = calculate_time();
	total_distance = get_total_distance(points);
	return ({
		"time": total_time,
		"distance": total_distance,
		"pace": (total_time / 60 / total_distance),
	});

if __name__ == "__main__":
	points_data = [
		(33, 44), (55, 33),
		(66, 45), (45, 33),
	]
	ret = track_summary(points_data);
	print(ret);

