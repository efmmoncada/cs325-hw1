# Emmanuel Moncada
# OSU ID: 933226429
# CS 325 - HW 1
# Jan 6 2021

import random, time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        
        # shift element to left until in correct position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    


def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def generate_array(n):
    arr = list()
    
    for i in range(n):
        arr.append(random.randint(0, 10000))
    
    return arr


if __name__ == "__main__":
    size = int(input("Enter the desired size of array (n): "))

    arr = generate_array(size)

    # inital time
    t0 = time.time()

    insertion_sort(arr)

    # end time
    t1 = time.time()

    print(f"== Array size: n = {len(arr)}")
    print(f"== Time to sort: {t1 - t0}")
