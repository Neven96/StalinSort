# -*- coding: utf-8 -*-
import random

def create_array(array_length, array_range):
    '''
    Creates an unsorted array of random length and number range
    Args:
        array_length (int): how long the unsorted array will be
        array_range (int): how wide the range of the numbers in the array will be
    Returns:
        list: an unsorted array of integers
    '''

    unsorted_array = []

    for i in range(1, array_length+1):
        unsorted_array.append(random.randint(1, array_range))

    return unsorted_array
