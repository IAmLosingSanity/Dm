def cocktail_sort(sample):          # O(n^2), best O(n), average O(n^2)
    left = 0
    right = len(sample) - 1

    while left <= right:
        for i in range(left, right, 1):
            if sample[i] > sample[i + 1]:
                sample[i], sample[i + 1] = sample[i + 1], sample[i]
        right -= 1

        for i in range(right, left, -1):
            if sample[i - 1] > sample[i]:
                sample[i], sample[i - 1] = sample[i - 1], sample[i]
        left += 1

    return sample

with open('input.txt', 'r') as input_file:
    numbers = [int(num) for num in input_file.readline().split()]

sorted_numbers = cocktail_sort(numbers)

with open('output.txt', 'w') as output_file:
    output_file.write(str(sorted_numbers) + '\n')
