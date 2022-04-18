class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self):
        mass = self._length * self._width * 25 * 5
        return mass

mass_road = Road(10000,5)
print(mass_road.mass_asphalt(), 'кг')
