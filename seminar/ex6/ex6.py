# Задание No6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Validator:
    """Class validator for rectangle"""
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Value {value} should be a number')
        if value is not None and value < 0:
            raise ValueError(f'Value {value} should be bigger than 0')

class Rectangle(object):
    """Class to represent a rectangle"""

    _length = Validator()
    _depth = Validator()

    def __init__(self, length, depth):
        """Initiate a rectangle"""
        self._length = length
        self._depth = depth

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        return (self.length + self.depth) * 2

    def area(self):
        """Calculate the area of a rectangle"""
        return self.length * self.depth

    def __add__(self, other):
        """Sum perimeters of two rectangles and get a new rectangle"""
        sum_perimeters = self.perimeter() + other.perimeter()
        sum_sides = sum_perimeters / 2
        return Rectangle(int(sum_sides / 2), int(sum_sides / 2))

    def __sub__(self, other):
        """Substuct perimeters if the result is bigger than 0 and return new Rectangle, else return None"""
        sub_perimeters: int
        sub_sides: int
        if self.perimeter() > other.perimeter():
            sub_perimeters = self.perimeter() - other.perimeter()
            sub_sides = sub_perimeters / 2
            return Rectangle(int(sub_sides / 2), int(sub_sides / 2))
        return None

    def __str__(self):
        """Get the string representation of the object"""
        return f'depth = {self.depth} length = {self.length}'

    def __repr__(self):
        """Get the formatted string representation of the object"""
        return f'Rectangle({self.depth}, {self.length})'

    def __eq__(self, other):
        """Check if two rectangles are equal"""
        first = self.area()
        second = other.area()
        return first == second

    def __ne__(self, other):
        """Check if two rectangles are not equal"""
        first = self.area()
        second = other.area()
        return first != second

    def __gt__(self, other):
        """Check if rectangle is bigger than another"""
        first = self.area()
        second = other.area()
        return first > second

    def __le__(self, other):
        """Check if rectangle is smaller or equal to another"""
        first = self.area()
        second = other.area()
        return first <= second

    def __lt__(self, other):
        """Check if rectange is smaller than another"""
        first = self.area()
        second = other.area()
        return first < second

    def __ge__(self, other):
        """Check if rectangle is bigger of equal to another"""
        first = self.area()
        second = other.area()
        return first >= second

    @property
    def length(self):
        return self._length

    @property
    def depth(self):
        return self._depth

    @length.setter
    def length(self, value):
        if value is None:
            raise ValueError(f'Length can not be None')
        elif value < 0:
            raise ValueError(f'Length can\'t be less than zero {value}')
        else:
            self._length = value

    @depth.setter
    def depth(self, value):
        if value is None:
            raise ValueError(f'Depth can not be None')
        elif value < 0:
            raise ValueError(f'Depth can\'t be less than zero {value}')
        else:
            self._depth = value


first_rec = Rectangle(10, 20)
second_rec = Rectangle(20, 10)
third_rec = Rectangle(30, 30)

print('first == second ', (first_rec == second_rec))
print('first != second ', first_rec != second_rec)
print('first != third ', first_rec != third_rec)
print('first > second ', first_rec > second_rec)
print('third > first ', third_rec > first_rec)
print('first <= second ', first_rec <= second_rec)
print('first <= third ', first_rec <= third_rec)
print('first < second ', first_rec < second_rec)
print('first < third ', first_rec < third_rec)
print('first >= second ', first_rec >= second_rec)
print('third >= second ', third_rec >= second_rec)

print(f'{first_rec = }')
print(f'{second_rec = }')
print(f'{third_rec = }')

print(first_rec.__dict__)

# validation_rec_1 = Rectangle(-20, 30)
# validation_rec_2 = Rectangle(-20, -30)
# validation_rec_3 = Rectangle(20, -30)
# validation_rec_4 = Rectangle('-20', 30)
# validation_rec_5 = Rectangle('-20', '30')
validation_rec_6 = Rectangle(20, '30')
