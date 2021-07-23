import math

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

def calculate_time():
	return (600);

def calculate_distance(points):
	print("called global");
	result = 0;
	point_len = len(points);
	i = 1;
	while (i < point_len):
		result += distance(points[i - 1], points[i]);
		i += 1;
	return (result);


def track_summary(points):
	def calculate_distance():
		print("called local");
		result = 0;
		nonlocal points
		point_len = len(points);
		i = 1;
		while (i < point_len):
			result += distance(points[i - 1], points[i]);
			i += 1;
		return (result);
	total_time = calculate_time();
	total_distance = globals()["calculate_distance"](points);
	#total_distance = calculate_distance(points);
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

