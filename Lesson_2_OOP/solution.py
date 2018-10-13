from random import randint

class Car:
	def __init__(self, name, max_speed, drag_coef, time_to_max):
		self.name = name
		self.max_speed = max_speed
		self.drag_coef = drag_coef
		self.time_to_max = time_to_max

	def get_car_speed(self, competitor_time, wind_speed):
		if competitor_time == 0:
			return 1
		else:
			_speed = (competitor_time / self.time_to_max) * self.max_speed
			if _speed > wind_speed:
				_speed -= (self.drag_coef * wind_speed)
			return _speed
	
class Weather:
	def __init__(self, max_wind_speed):
		self.__max_wind_speed = max_wind_speed
	
	@property
	def get_wind_speed(self):
		wind_speed = randint(0, self.__max_wind_speed)
		return wind_speed

class Competition:
	instance = None
	def __new__(cls, *args, **kwargs):
		if cls.instance == None:
			cls.instance = super().__new__(cls)
			return cls.instance
		else:
			raise Exception("Не может быть создано более одного экземпляра")
		
	def __init__(self, distance):
		self.distance = distance

	def start(self, competitors, weather):
		for car in competitors:
			competitor_time = 0
			for _ in range(self.distance):
				wind_speed = weather.get_wind_speed
				_speed = Car.get_car_speed(car, competitor_time, wind_speed)
				competitor_time += float(1) / _speed

			print("Car <%s> result: %f" % (car.name, competitor_time))

ferrary = Car("ferrary", 340, 0.324, 26)
bugatti = Car("bugatti", 407, 0.39, 32)
toyota = Car("toyota", 180, 0.25, 40)
lada = Car("lada", 180, 0.32, 56)
sx4 = Car("sx4", 180, 0.33, 44)

weather = Weather(max_wind_speed = 20)

competitors = (ferrary, bugatti, toyota, lada, sx4)
competition = Competition(10000)
competition.start(competitors, weather)
