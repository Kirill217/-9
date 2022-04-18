class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} тронулась'.format(self.name))

    def stop(self):
        print('{} тормозит'.format(self.name))

    def turn(self, direction):
        print('{} поехала {}'.format(self.name, direction))

    def show_speed(self):
        print('текущая скорость {}'.format(self.speed))

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('не гони брат, тебя дома ждут')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('не гони брат, тебя дома ждут')

class Police(Car):
    pass

town_car = TownCar(80, 'yellow', 'KIA', None)
sport_car = SportCar(320, 'red', 'Mc.Laren', None)
work_car = WorkCar(60, 'blaeck', 'КАМАЗ', None)
police_car = Police(220, 'police', 'Ford', True)

town_car.show_speed()
sport_car.turn('Left')
work_car.show_speed()
police_car.go()