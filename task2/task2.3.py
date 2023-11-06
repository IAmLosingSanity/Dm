def sequential_search(array, element):
    k = 0
    for i in range(len(array)):
        k += 1
        if array[i] == element:
            return k
    return -1

def binary_search(array, element):
    k = 0
    array.sort()
    low = 0
    high = len(array) - 1
    while low <= high:
        k += 1
        mid = (low + high) // 2
        if array[mid] == element:
            return k
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def interpolation_search(array, element):
    k = 0
    low = 0
    high = len(array) - 1

    while array[low] < element and array[high] > element:
        k += 1
        if array[high] == array[low]:
            break

        mid = low + ((element - array[low]) * (high - low)) // (array[high] - array[low])

        if array[mid] < element:
            low = mid + 1
        elif array[mid] > element:
            high = mid - 1
        else:
            return k

    if array[low] == element:
        return k
    if array[high] == element:
        return k

    return -1

# Read the input file
with open('input.txt', 'r') as file:
    array = [int(num) for num in file.read().split()]

# Perform sequential search
sequential_comparisons = []
for i in range(1, len(array) + 1):
    k = sequential_search(array, i)
    sequential_comparisons.append(k)

# Perform binary search
binary_comparisons = []
for i in range(1, len(array) + 1):
    k = binary_search(array, i)
    binary_comparisons.append(k)

# Perform interpolation search
interpolation_comparisons = []
for i in range(1, len(array) + 1):
    k = interpolation_search(array, i)
    interpolation_comparisons.append(k)

# Calculate the average number of comparisons
average_sequential_comparisons = sum(sequential_comparisons) / len(array)
average_binary_comparisons = sum(binary_comparisons) / len(array)
average_interpolation_comparisons = sum(interpolation_comparisons) / len(array)

# Write the average number of comparisons to the output file
with open('output.txt', 'w') as file:
    file.write(f"Average number of comparisons for sequential search: {average_sequential_comparisons}\n")
    file.write(f"Average number of comparisons for binary search: {average_binary_comparisons}\n")
    file.write(f"Average number of comparisons for interpolation search: {average_interpolation_comparisons}\n")