# Emmanuel Moncada
# OSU ID: 933226429
# CS 325 - HW 1
# Jan 6 2021

import random, time

def merge_sort(arr):
    if len(arr) > 1:
        # find middle
        mid = len(arr)//2

        # split
        left = arr[:mid]
        right = arr[mid:]

        # recursive call
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # check for leftovers
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


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

    merge_sort(arr)

    # end time
    t1 = time.time()

    print(f"== Array size: n = {len(arr)}")
    print(f"== Time to sort: {t1 - t0}")


