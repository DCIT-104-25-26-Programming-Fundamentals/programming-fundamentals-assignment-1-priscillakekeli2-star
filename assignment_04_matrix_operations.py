# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

# Function to read a matrix from the user
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} values.")
    return matrix


# Function to display a matrix neatly
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# Part A: Transpose a Matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# Part B: Add Two Matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)

    return result


# Part C: Multiply Two Matrices
def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []

    for i in range(rowsA):
        new_row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


# ===========================
# MAIN PROGRAM
# ===========================

print("===== PART A: Transpose a Matrix =====")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix:")
matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


print("\n===== PART B: Add Two Matrices =====")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix 1:")
matrix1 = read_matrix(rows, cols)

print("Enter Matrix 2:")
matrix2 = read_matrix(rows, cols)

print("\nMatrix 1:")
display_matrix(matrix1)

print("\nMatrix 2:")
display_matrix(matrix2)

print("\nSum of Matrices:")
display_matrix(add_matrices(matrix1, matrix2))


print("\n===== PART C: Multiply Two Matrices =====")
rowsA = int(input("Enter number of rows for Matrix A: "))
colsA = int(input("Enter number of columns for Matrix A: "))

print("Enter Matrix A:")
matrixA = read_matrix(rowsA, colsA)

rowsB = int(input("Enter number of rows for Matrix B: "))
colsB = int(input("Enter number of columns for Matrix B: "))

while colsA != rowsB:
    print("Matrix multiplication is not possible.")
    print("The number of columns in Matrix A must equal the number of rows in Matrix B.")
    rowsB = int(input("Re-enter number of rows for Matrix B: "))
    colsB = int(input("Re-enter number of columns for Matrix B: "))

print("Enter Matrix B:")
matrixB = read_matrix(rowsB, colsB)

print("\nMatrix A:")
display_matrix(matrixA)

print("\nMatrix B:")
display_matrix(matrixB)

print("\nProduct of Matrix A × Matrix B:")
display_matrix(multiply_matrices(matrixA, matrixB))