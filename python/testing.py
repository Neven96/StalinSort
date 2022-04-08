from stalinsort import stalin_sort
from random_array_gen import create_array

def main():
    unsorted_array = create_array(100, 100)
    sorted_array = stalin_sort(unsorted_array)

    print(f"Unsorted: {unsorted_array}")
    print(f"Sorted: {sorted_array}")

    unsorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorted_array = stalin_sort(unsorted_array)

    print(f"Unsorted: {unsorted_array}")
    print(f"Sorted: {sorted_array}")

if __name__ == '__main__':
    main()
