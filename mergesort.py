# Emmanuel Moncada
# OSU ID: 933226429
# CS 325 - HW 1
# Jan 6 2021

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


if __name__ == "__main__":
    with open("./data.txt") as file:
        for line in file:
            
            # create an array from the input line
            arr = line.split()

            # discard line length
            arr.pop(0)

            # convert array of strings to ints
            arr = [int(i) for i in arr]

            # sort and print list
            merge_sort(arr)
            print_list(arr)
