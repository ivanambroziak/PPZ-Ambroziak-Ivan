import time
def fibonacci_seq_generator():
    a = 0
    b = 1

    while True:
        yield a
        t = a
        a = b
        b = t + b

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд.")
        return result
    return wrapper

@timer_wrapper
def prime_num_getter(n):
    generator = fibonacci_seq_generator()
    prime_count = 0
    while prime_count < n:
        number = next(generator)
        if is_prime(number):
            print(number, end=" ")
            prime_count += 1
    print()

def main():
    while True:
        count = int(input("Введіть кількість чисел: "))
        if not count:
            break
        prime_num_getter(count)

main()