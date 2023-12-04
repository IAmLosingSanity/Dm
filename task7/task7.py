def select_part(lst, k):
    def partition(lst, left, right):
        pivot = lst[right]
        i = left - 1
        for j in range(left, right):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i+1], lst[right] = lst[right], lst[i+1]
        return i + 1

    left = 0
    right = len(lst) - 1
    lst.append(float('inf'))
    found = False
    while not found:
        v = partition(lst, left, right)
        if k < v:
            right = v - 1
        elif k == v:
            found = True
            result = v
        else:
            left = v + 1
    return result

arr = [20, 12, 18, 16, 24, 10, 22, 14]
k = len(arr) // 2  # Индекс медианного элемента
median = select_part(arr, k)
print(f"Медиана массива: {arr[median]}")