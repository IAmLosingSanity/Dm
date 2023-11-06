def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * determinant([row[:i] + row[i+1:] for row in matrix[1:]])
        return det

# def det3(matrix):
#     if len(matrix) == 1:
#         return matrix[0][0]
#     else:
#         det = 0
#         for i in range(len(matrix)):
#             det += matrix[0][i] * matrix [1][i+1]

with open("input.txt") as f:
    matrix = [list(map(int, line.split())) for line in f]

print(determinant(matrix))
input()