def determinant(matrix):            #O(n!)
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * determinant([row[:i] + row[i+1:] for row in matrix[1:]])
        return det

def determinant3(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * determinant3([row[:i] + row[i+1:] for row in matrix[1:]])
        return det

def determinant1123(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)
    return det

with open("input.txt") as f:
    matrix = [list(map(int, line.split())) for line in f]

with open("input2.txt") as o:
    matrix2 = [list(map(int, line.split())) for line in o]
    matrix3 = matrix2.copy()

print(determinant(matrix))
print(determinant3(matrix2))
print(determinant1123(matrix3))
input()