class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('рисование ручкой')

class Pencil(Stationery):
    def draw(self):
        print('рисование карандашом')

class Handle(Stationery):
    def draw(self):
        print('рисование маркером')

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()