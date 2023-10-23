#def function that recursively calculates matrix determinant
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * determinant([row[:i] + row[i+1:] for row in matrix[1:]])
        return det

with open("input.txt") as f:
    #read square matrix from file
    matrix = [list(map(int, line.split())) for line in f]

print(determinant(matrix))
input()