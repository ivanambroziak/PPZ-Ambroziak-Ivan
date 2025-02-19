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

# Task 3
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


###

#task1(1,11) # Вивести усі числа від 1 до 10.
#task1(2, 21,2)  # Вивести усі парні числа від 1 до 20.
#task1(10, 0, -1) # Вивести усі числа від 10 до 1

#task2(1, 100)

ivas = Student("Ivas")  # Task 3
ivas.greet()
ivas.is_student()