# Задание No3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.
import math


class Factorial:
    def __init__(self, start=1, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.factorial = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.factorial < self.stop:
            return self.get_factorial()
        raise StopIteration

    def get_factorial(self):
        calc_fact = math.factorial(self.factorial)
        self.factorial = self.factorial + self.step
        return calc_fact


factorial = Factorial(1, 34, 5)
print(next(factorial))
for c in factorial:
    print(c)
