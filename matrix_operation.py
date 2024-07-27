import numpy as np 

def transpose_matrix(matrix):
    return np.transpose(matrix)

def multiply_matrix(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

matrix1 = np.array([
    [1,2,3],
    [4,5,6]
])

matrix2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

transposed_matrix1 = transpose_matrix(matrix1)
print(" transpose of matrix1 is ", transposed_matrix1)

if matrix1.shape[1] == matrix2.shape[0]:
    product_matrix = multiply_matrix(matrix1, matrix2)
    print("\n product of matrix1 and matrix 2 is :", product_matrix)
else:
    print("\n incompatible dimension of matrix try again")