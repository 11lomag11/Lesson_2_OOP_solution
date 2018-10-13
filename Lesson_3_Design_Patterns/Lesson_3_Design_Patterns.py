from random import randint, random
from math import ceil
import copy
from abc import ABCMeta, abstractmethod

class IOperator:

	__metaclass__ = ABCMeta

	@abstractmethod
	def get_damage(self):
		pass
	

class Damage(IOperator):
	
	def get_damage(self):
		rand = random()
		if rand <= 0.015: return 1
		else: return 0
	

class Car:
	def __init__(self, name, max_speed, drag_coef, time_to_max, health_points):
		self.name = name
		self.max_speed = max_speed
		self.drag_coef = drag_coef
		self.time_to_max = time_to_max
		self.health_points = health_points

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


class Wrapper(IOperator):
	def __init__(self, obj):
		self.obj = obj

	def get_damage(self):
		rand = random()
		if rand <= 0.00025: 
			return self.obj.get_damage() + 75
		else:	
			return self.obj.get_damage()
	
	def start(self, competitors, weather):
		return self.obj.start(competitors, weather)


class Competition():
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
				car.health_points -= critical_damage.get_damage()
				competitor_time += float(1) / _speed
			results.take_result(car.name, competitor_time, car.health_points)
			

class Observer(metaclass=ABCMeta):
    """
    Абстрактный наблюдатель
    """
    @abstractmethod
    def update(self, message):
        """
        Получение нового сообщения
        """
        pass


class Observable(metaclass=ABCMeta):
    """
    Абстрактный наблюдаемый
    """

    def __init__(self):
        self.observers = []  

    def register(self, observer):
        """
        Регистрация нового наблюдателя на подписку
        """
        self.observers.append(observer)

    def notify_observers(self, message):
        """
        Передача сообщения всем наблюдателям, подписанным на события
        данного объекта наблюдаемого класса
        """
        for observer in self.observers:
            observer.update(message)


class Results(Observable):

	competitors = []

	def take_result(self, name, time, hp):
		if hp <= 0:
			return self.competitors.append(f"{name} выведна из строя")
		string = f"{name} финиширует за: {(ceil(time*100)/100)} сек. С остатком здоровья: {hp}"
		self.competitors.append(string)

	def mailing_result(self):
		for competitor in self.competitors:
			print(competitor)


class Viewers(Observer):
	def __init__(self, name):
		self.name = name

	def update(self, message):
		print('{}'.format(message))


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Регистрируем объект"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Отмена регистрации"""
        del self._objects[name]

    def clone(self, names, **attr):
        """Клонируем зарегистрированный объект и обновляем внутренний словарь атрибутов"""
        obj = copy.deepcopy(self._objects.get(names))
        obj.__dict__.update(attr)
        return obj


ferrary = Car("Ferrary", 340, 0.324, 26, 560)
prototype = Prototype()
prototype.register_object('objecta', ferrary)
bugatti = prototype.clone('objecta', name = "Bugatti", max_speed  = 407, drag_coef = 0.39, time_to_max = 32, health_points = 480)
toyota = prototype.clone('objecta', name="Toyota", max_speed  = 180, drag_coef = 0.25, time_to_max = 40, health_points = 380)
lada = prototype.clone('objecta', name="Lada", max_speed  = 180, drag_coef = 0.32, time_to_max = 56, health_points = 200)
sx4 = prototype.clone('objecta', name="SX4", max_speed  = 180, drag_coef = 0.33, time_to_max = 44, health_points = 800)

weather = Weather(max_wind_speed = 20)

results = Results()

damage = Damage()
critical_damage = (Wrapper(damage))

competitors = (ferrary, bugatti, toyota, lada, sx4)
competition = Competition(10000)
competition.start(competitors, weather)

results.register(Viewers("Зритель"))
results.mailing_result()
