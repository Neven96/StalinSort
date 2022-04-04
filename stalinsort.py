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

def stalinSort(unsorted_array):
    '''
    Sorts an array, Stalin method
    Args:
        unsorted_array (list): the unsorted array
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


def main():
    unsorted_array = create_array(100, 100)
    sorted_array = stalinSort(unsorted_array)

    print("Unsorted: ",unsorted_array)
    print("Sorted: ",sorted_array)

if __name__ == '__main__':
    main()
