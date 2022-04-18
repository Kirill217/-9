from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = ('Крассный', 7), ('Жёлтый', 2), ('Зелёный', 15)

    def switching(self):
        for color, sec in self.__color:
            print(color, 'У тебя есть {} секунд'.format(sec))
            sleep(sec)

switching_traffic_lights = TrafficLight()
switching_traffic_lights.switching()
