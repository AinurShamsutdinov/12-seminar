# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
#   недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов
#   вместе взятых.
import csv


class StudentName:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Value {value} should be string')
        if not value.isalpha():
            raise ValueError(f'Value {value} should contain only letters')
        if not str(value[0]).isupper():
            raise ValueError(f'Value {value} should have first letter in uppercase')


class Grade:

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Value {value} should be integer')
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f'Value {value} should be between {self.min_value} and {self.max_value}')


class SubjectName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        is_subject_in_file = False
        with open('subjects.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if value == row[0]:
                    is_subject_in_file = True
                    break
        if not is_subject_in_file:
            raise ValueError(f'Value {value} should be in subject.csv file')


class Student:
    subjects = dict()
    tests = dict()
    list_sub = list()
    name = StudentName()
    subject = SubjectName()
    grade = Grade(2, 5)
    test = Grade(1, 100)

    def __init__(self, name):
        self.name = name
        self.subjects = dict()
        self.tests = dict()

    def __repr__(self):
        return f'Student(name={self.name}, grade={self.grade}, tests={self.tests})'

    def add_subject(self, subject, grade):
        self.subject = subject
        self.grade = grade
        if self.subject in self.subjects.keys():
            self.subjects[self.subject].append(self.grade)
        else:
            self.subjects[self.subject] = list()
            self.subjects[self.subject].append(self.grade)

    def add_tests(self, subject, grade):
        self.subject = subject
        if subject in self.tests:
            self.tests[self.subject].append(grade)
        else:
            self.tests[self.subject] = list()
            self.tests[self.subject].append(grade)

    def get_average_test(self):
        average_test = dict()
        average_subj = dict()
        for key, item in self.tests.items():
            average_test[key] = sum(item) / len(item)
        for key, item in self.subjects.items():
            average_subj[key] = sum(item) / len(item)
        return f'Average test scores {average_test}\nAverage subject scores {average_subj}'


if __name__ == '__main__':
    student = Student('Parker')
    student.add_subject('math', 4)
    student.add_subject('math', 5)
    student.add_subject('history', 3)
    student.add_subject('history', 4)
    student.add_subject('chemistry', 4)
    student.add_subject('chemistry', 5)
    student.add_subject('math', 3)
    student.add_subject('math', 4)
    student.add_tests('chemistry', 89)
    student.add_tests('chemistry', 67)
    student.add_tests('chemistry', 75)
    student.add_tests('chemistry', 89)
    student.add_tests('math', 72)
    student.add_tests('math', 67)
    student.add_tests('math', 75)
    student.add_tests('math', 72)
    print(student.get_average_test())
