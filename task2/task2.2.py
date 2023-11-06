def linearSearch(list, value):    #O(n)
    k = 0
    for i in range(len(list)):
        k += 1
        if list[i] == value:
            return k
    return -1

def binarySearch(list, value):    #O(log n)
    k = 0
    list.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        k += 1
        mid = (low + high) // 2
        if list[mid] == value:
            return k
        elif list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def interpolation_search(sorted_array, to_find):    #O(log log n) -> O(n)
    k = 0
    low = 0
    high = len(sorted_array) - 1

    while sorted_array[low] < to_find and sorted_array[high] > to_find:
        k += 1
        if sorted_array[high] == sorted_array[low]:
            break

        mid = low + ((to_find - sorted_array[low]) * (high - low)) // (sorted_array[high] - sorted_array[low])

        if sorted_array[mid] < to_find:
            low = mid + 1
        elif sorted_array[mid] > to_find:
            high = mid - 1
        else:
            return k

    if sorted_array[low] == to_find:
        return k
    if sorted_array[high] == to_find:
        return k

    return -1

with open('input.txt') as f:
    #read list from file
    l = list(map(int, f.readline().split()))
    lsorted = l.copy()
    lsorted.sort()
    print(l)
    print(lsorted)
    with open('output.txt', 'w') as o:
        o.write(str(linearSearch(l, 3)) + '\n')
        o.write(str(binarySearch(lsorted, 3)) + '\n')
        o.write(str(interpolation_search(lsorted, 3)) + '\n')