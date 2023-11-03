# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:57:46 2023

@author: prome
"""

def fibonacci_recursion(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

def fibonacci(n):
    fibonacci_value = fibonacci_recursion(n)
    print("The {count}. Fibonacci number is {number}.".format(count = n, number = fibonacci_value))
    return fibonacci_value
    
print(fibonacci(10))