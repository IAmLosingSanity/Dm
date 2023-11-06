def cocktail_sort(numbers):
    n = len(numbers)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end + 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # Backward pass
        end -= 1

        for i in range(end, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start += 1

    return numbers

def count_comparisons(numbers):
    comparisons = 0
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            comparisons += 1
    return comparisons

with open('input.txt', 'r') as input_file:
    numbers = [int(num) for num in input_file.readline().split()]

sorted_numbers = cocktail_sort(numbers)
comparisons = count_comparisons(numbers)

with open('output.txt', 'w') as output_file:
    output_file.write(str(sorted_numbers) + '\n')
    output_file.write(str(comparisons) + '\n')