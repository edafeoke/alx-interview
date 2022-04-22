#!/usr/bin/python3
'''
a module that contains a that contains a function that
calculates the fewest number of operations needed to result
in exactly n H characters in the file
'''


def minOperations(n):
    '''
    returns minimum operations
    '''
    min_operation = 0
    index = 2
    if n < 2:
        return 0
    while (index < n + 1):
        # check if problem can be broken into smaller problem
        while n % index == 0:
            # if yes then add no of smaller problems to result
            min_operation += index
            # create smaller problem
            n /= index
        index += 1
    return min_operation
