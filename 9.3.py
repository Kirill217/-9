class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        return f'Имя: {self.name}. Фамилия: {self.surname}. Должность: {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus

piople_work = Position('Kirill', 'Silimov', 'engineer', {'wage': 65000, 'bonus': 15000})
print(piople_work.get_full_name())
print(piople_work.get_total_income())