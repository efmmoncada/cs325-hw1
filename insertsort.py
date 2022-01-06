
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


if __name__ == "__main__":
    with open("data.txt") as file: 
        for line in file:
            
            # create an array from the input line
            arr = line.split()

            # discard line length
            arr.pop(0)

            # convert array of strings to ints
            arr = [int(i) for i in arr]

            # sort and print list
            insertion_sort(arr)
            print_list(arr)
