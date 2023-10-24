def linearSearch(list, value):    #O(n)
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1

def binarySearch(list, value):    #O(log n)
    list.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def interpolation_search(sorted_array, to_find):    #O(log log n) -> O(n)
    low = 0
    high = len(sorted_array) - 1

    while sorted_array[low] < to_find and sorted_array[high] > to_find:
        if sorted_array[high] == sorted_array[low]:
            break

        mid = low + ((to_find - sorted_array[low]) * (high - low)) // (sorted_array[high] - sorted_array[low])

        if sorted_array[mid] < to_find:
            low = mid + 1
        elif sorted_array[mid] > to_find:
            high = mid - 1
        else:
            return mid

    if sorted_array[low] == to_find:
        return low
    if sorted_array[high] == to_find:
        return high

    return -1

with open("input.txt") as f:
    #read list from file
    l = list(map(int, f.readline().split()))
    