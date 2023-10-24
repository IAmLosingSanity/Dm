def linearSearch(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1

def binarySearch(list, value):
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

def interpolationSearch(list, value):
    

with open("input.txt") as f:
    #read list from file
    l = list(map(int, f.readline().split()))
    
