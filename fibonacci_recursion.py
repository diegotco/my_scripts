"""Taken from https://www.freecodecamp.org/news/how-to-learn-programming/?utm_source=pocket_mylist"""

import timeit

start_time = timeit.timeit()


def fib():
    x1 = 0
    x2 = 1

    def get_next_number():
        nonlocal x1, x2
        x3 = x1 + x2
        x1, x2 = x2, x3
        return x3
    return get_next_number


fibonacci = fib()

for i in range(2, 5):
    num = fibonacci()
    print(f'The {i}th Fibonacci number is {num}')

end_time = timeit.timeit()

print(end_time - start_time)
