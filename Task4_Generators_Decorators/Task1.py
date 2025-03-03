def fibonacci_seq_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

generator = fibonacci_seq_generator()

print("Щоб вивести наступне натисніть Enter.")
print("Щоб закінчити роботу генератора введіть 1: ")

while True:
    i = input()
    if i == "1":
        break
    else:
        print(next(generator), end=" ")
