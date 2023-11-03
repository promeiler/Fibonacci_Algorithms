# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:32:29 2023

@author: prome
"""

def fibonacci(n):
    fibonacci_dict = {}
    current_fibonacci = 0
    while current_fibonacci <= n:
        if current_fibonacci in [0, 1]:
            fibonacci_value = current_fibonacci
        else:
            fibonacci_value = 0
        if current_fibonacci > 0:
            last_fibonacci = current_fibonacci - 1
            fibonacci_value += fibonacci_dict.get(last_fibonacci)
        if current_fibonacci > 1:
            last2_fibonacci = current_fibonacci - 2
            fibonacci_value += fibonacci_dict.get(last2_fibonacci) 
        fibonacci_dict[current_fibonacci] = fibonacci_value
        current_fibonacci += 1
    print("The {count}. Fibonacci number is {number}.".format(count = n, number = fibonacci_dict[n]))
    return fibonacci_dict[n]
    
    
fibonacci(10)