# -*- coding: utf-8 -*-

def stalin_sort(unsorted_array):
    '''
    Sorts an array, Stalin method
    Args:
        unsorted_array (list): an array for sorting
    Returns:
        list: the properly sorted array
    '''
    sorted_array = []
    i = 0
    j = 1
    sorted_array.append(unsorted_array[0]) #First element is alway correct

    while j < len(unsorted_array):
        if sorted_array[i] <= unsorted_array[j]:
            sorted_array.append(unsorted_array[j])
            i += 1
            j += 1
        else:
            j += 1

    return sorted_array
