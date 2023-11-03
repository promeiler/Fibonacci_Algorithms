# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:36:03 2023

@author: prome
"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_value(self, new_value):
        self.value = new_value
        print("Set value to {}".format(new_value))
        
    def set_next_node(self, new_next_node):
        self.next_node = new_next_node
        
class FibonacciList:
    def __init__(self, n):
        fibonacci_0 = Node(0)
        fibonacci_1 = Node(1, fibonacci_0)
        self.head_node = fibonacci_1
        while n > 1:
            self.add_to_head()
            n -= 1
        
    def stringfy(self):
        string = ""
        current_node = self.head_node
        while current_node != None:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string
    
    def add_to_head(self):
        if self.head_node == None:
            new_node = Node(0)
            self.head_node = new_node
            return
        elif self.head_node.get_next_node() == None:
            new_node = Node(1, self.head_node)
            self.head_node = new_node
            return
        else:
            next_node = self.head_node
            next_next_node = next_node.get_next_node()
            new_node = Node(next_node.get_value() + next_next_node.get_value())
            new_node.set_next_node(next_node)
            self.head_node = new_node
            return
        
    def peek(self):
        return self.head_node.get_value()
            
def fibonacci(n):
    fibonacci_number = FibonacciList(n).peek()
    print("The {count}. Fibonacci number is {number}.".format(count = n, number = fibonacci_number))
    return 
        
fibonacci(100)
