from itertools import permutations

# Sort the permutations using the quicksort algorithm and count comparisons
def quicksort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    left_sorted, left_comparisons = quicksort(left)
    right_sorted, right_comparisons = quicksort(right)
    comparisons += left_comparisons + right_comparisons
    sorted_array = right_sorted + middle + left_sorted  # Sort in descending order
    return sorted_array, comparisons + len(arr) - 1

# Generate permutations of the numbers 1 to 5

with open('input.txt', 'r') as file:
    N = int(file.read())

# Генерация всех возможных перестановок
permutations = list(permutations(range(1, N + 1)))

# Sort the permutations and write them to output.txt
with open('output.txt', 'w') as file:
    sorted_permutations = sorted(permutations, key=lambda perm: quicksort(list(perm))[1], reverse=True)
    for perm in sorted_permutations:
        sorted_array, comparisons = quicksort(list(perm))
        file.write(f'{perm} (comparisons: {comparisons})\n')