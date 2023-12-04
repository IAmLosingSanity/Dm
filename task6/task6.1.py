import itertools

# Функция быстрой сортировки с подсчетом сравнений
def quicksort(arr, compare_count=[0]):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            compare_count[0] += 1
            if x < pivot:
                less.append(x)
            else:
                greater.append(x)
        return quicksort(less, compare_count) + [pivot] + quicksort(greater, compare_count)

# Чтение размера массива из файла
with open('input.txt', 'r') as file:
    N = int(file.read())

# Генерация всех возможных перестановок
permutations = list(itertools.permutations(range(1, N + 1)))

# Инициализация переменных для отслеживания максимального количества сравнений
max_compare_count = 0
arrays_with_max_comparisons = []

# Выполнение сортировки для каждой перестановки и подсчет количества сравнений
for permutation in permutations:
    compare_count = [0]
    sorted_array = quicksort(list(permutation), compare_count)
    if compare_count[0] > max_compare_count:
        max_compare_count = compare_count[0]
        arrays_with_max_comparisons = [(sorted_array, compare_count[0])]
    elif compare_count[0] == max_compare_count:
        arrays_with_max_comparisons.append((sorted_array, compare_count[0]))

# Запись результатов в файл
with open('output.txt', 'w') as file:
    for array, num_comparisons in arrays_with_max_comparisons:
        file.write(' '.join(map(str, array)) + ' ' + str(num_comparisons) + '\n')

    # Дополнительно сохраняем количество сравнений для всех перестановок
    file.write('\n')
    for permutation in permutations:
        compare_count = [0]
        quicksort(list(permutation), compare_count)
        file.write(' '.join(map(str, permutation)) + ' ' + str(compare_count[0]) + '\n')