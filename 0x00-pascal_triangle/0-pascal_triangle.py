#!/usr/bin/python3
'''
A module that contains the pascal_triangle function
'''

from math import factorial


def combination(a, b):
    '''Returns nCr of two arguments'''
    return int(factorial(a) / (factorial(b) * factorial(a - b)))


def pascal_triangle(n):
    '''
    A function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    '''

    pascal_list = []

    if n <= 0:
        return pascal_list

    for i in range(n):
        y = 0
        row = []
        for j in range(i + 1):
            row.append(combination(i, y))
            y += 1
        pascal_list.append(row)
    return pascal_list
