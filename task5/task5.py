def shellSort(arr):
    comparisons = 0
    n = len(arr)

    # Gap sequence 1: hs = 2^s - 1, where 0 <= s < log2(n)
    gap_sequence_1 = []
    s = 0
    while (2 ** s - 1) < n:
        gap_sequence_1.append(2 ** s - 1)
        s += 1

    # Gap sequence 2: hs = 3^s - 1, where 0 <= s < log3(2n+1) - 1
    gap_sequence_2 = []
    s = 0
    while (3 ** s - 1) < (2 * n + 1):
        gap_sequence_2.append(3 ** s - 1)
        s += 1

    # Sort using gap sequence 1
    for gap in reversed(gap_sequence_1):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            comparisons += 1
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparisons += 1
            arr[j] = temp

    # Sort using gap sequence 2
    for gap in reversed(gap_sequence_2):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            comparisons += 1
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparisons += 1
            arr[j] = temp

    return arr, comparisons


# Read input array from input.txt
with open("input.txt") as file:
    input_array = list(map(int, file.readline().split()))

# Perform Shell sort and get the sorted array and number of comparisons
sorted_array, comparisons = shellSort(input_array)

# Write the sorted array and number of comparisons to output.txt
with open("output.txt", "w") as file:
    file.write(" ".join(map(str, sorted_array)) + "\n")
    file.write(str(comparisons))