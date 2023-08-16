# Задание No1
# 📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
#
# Задание No2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.


import json
from collections import OrderedDict


class Factorial:

    def __init__(self, num_elements):
        self.storage = OrderedDict()
        self.num_elements = num_elements

    def __call__(self, value):
        factorial = 1
        for i in range(1, value + 1):
            factorial *= i
        if self.num_elements > len(self.storage):
            self.storage[value] = factorial
        elif self.num_elements == len(self.storage):
            self.storage.popitem(last=False)
            self.storage[value] = factorial
        return factorial

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        json_string = json.dumps(self.storage, indent=4)
        with open('json_data.json', 'w') as outfile:
            outfile.write(json_string)
        print(json_string)

    def get_factorials(self):
        return self.storage


with Factorial(2) as fact:
    print(fact(3))
    print(fact(4))
    print(fact(6))
    print(fact(10))
    print(fact.get_factorials())
