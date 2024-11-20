# math_helpers.py
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(int(digit) for digit in str(n)))
