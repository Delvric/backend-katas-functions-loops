#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "delvric"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    result = 0
    for i in range(abs(y)):
        result = add(result, x)
    if y < 0 or x < 0:
        result = -abs(result)
    return result


def power(x, n):
    """Raise x to power n, where n >= 0"""
    result = x
    if n >= 0:
        arr = range(1, n)
        for i in arr:
            result = multiply(result, x)
    return result


def factorial(x):
    """Compute factorial of x, where x > 0"""
    result = 1
    for i in range(1, x+1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # [0,1,1,2,3,5,8]: 13 to this function, and it will output will return that fib element
    arr = [0, 1, 1]
    for i in range(2, n):
        arr.append(arr[-1] + arr[-2])
    return arr[n-1]


def main():
    print(add(2, 4))
    print(multiply(6, -8))
    print(power(3, 4))
    print(factorial(4))
    print(fibonacci(8))


if __name__ == '__main__':
    # your code to call functions above
    print("hello world")
    main()
