# Task 1
# Вивести усі числа від 1 до 10.
# Вивести усі парні числа від 1 до 20.
# Вивести усі числа від 10 до 1

def task1(start, end, step = 1):
    print("Task 1:")
    for i in range(start, end, step):
        print(i, end=", ")
    print()

# Task 2
# Створити таблицю множення від 1 до 10

def task2(multiplier1 = 1, multiplier2 = 11):
    print("Task 2:")
    for i in range(multiplier1, multiplier2):
        print(f"Таблиця множення від {multiplier1} до {multiplier2 - 1}")
        for j in range(multiplier1, multiplier2):
            print(f"{i} × {j} = {i * j}")

#  Task 3
#  Створити клас Person. Властивості - name.
#  Функції - greet. При виклику функції мусить повертатись рядок
#  “Привіт, мене звуть <ім’я>”.
#  Створити клас Student, який успадковує Person.
#  Функції: is_student -> bool (виведення статусу студента).
#  Викликати усі методи для класу Student

class Person:
    def __init__(self, name = ""):
        self.name = name

    def greet(self):
        print(f"Привіт, мене звуть {self.name}")

class Student(Person):
    def is_student(self):
        print(True)

# Task 4
# Створити абстрактний базовий клас (ABC) Shape з абстрактним методом area().
# Створити клас Circle, який успадковує Shape. Властивості - radius.
# Функції - area(). Створити клас Rectangle, який успадковує Shape.
# Властивості - width та height. Функції - area()

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius ** 2
        return area

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area


#Task 1
task1(1,11)    # Вивести усі числа від 1 до 10.
task1(2, 21,2)     # Вивести усі парні числа від 1 до 20.
task1(10, 0, -1)   # Вивести усі числа від 10 до 1

#Task 2
task2(1, 11)   # Створити таблицю множення від 1 до 10

#Task 3
ivas = Student("Ivas")  # Task 3
ivas.greet()
ivas.is_student()

#Task 4
circle1 = Circle(3)
print(circle1.area())
rectangle1 = Rectangle(2, 4)
print(rectangle1.area())
