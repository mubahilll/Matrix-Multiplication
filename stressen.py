from prettytable import PrettyTable
import time
import random

def banner():
    CYAN = "\033[36m"
    font = f"""{CYAN}
		** Stressen's Matrix Multiplication **
    -> Only works for square matrix
    -> Both matrices will have same number of rows and column
    -> Matrices are populated with random values\n"""
    print(font)


#Function to populate table using random values
def populate(m, r, c):
    for i in range(r):  
        a =[]
        for j in range(c):      # A for loop for column entries
            a.append(int(random.randrange(1,10)))
        m.append(a)
    return m   

#Function to print the matrix
def print_matrix(matrix, title="Matrix"):
    table = PrettyTable()
    table.title = title
    table.field_names = [f"Col {i+1}" for i in range(len(matrix[0]))]
    
    for row in matrix:
        table.add_row(row)

    print(table)

#Function to add two matrices
def add_matrix(matrix_A, matrix_B, matrix_C, split_index): 
	for i in range(split_index): 
		for j in range(split_index): 
			matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j] 

#Function to initialize matrix with zeros
def initWithZeros(a, r, c): 
	for i in range(r): 
		for j in range(c): 
			a[i][j] = 0

#Function to multiply two matrices
def multiply_matrix(matrix_A, matrix_B): 
	col_1 = len(matrix_A[0]) 
	row_1 = len(matrix_A) 
	col_2 = len(matrix_B[0]) 
	row_2 = len(matrix_B) 

	if (col_1 != row_2): 
		print("\nError: The number of columns in Matrix A must be equal to the number of rows in Matrix B\n") 
		return 0

	result_matrix_row = [0] * col_2
	result_matrix = [[0 for x in range(col_2)] for y in range(row_1)] 

	if (col_1 == 1): 
		result_matrix[0][0] = matrix_A[0][0] * matrix_B[0][0] 

	else: 
		split_index = col_1 // 2

		row_vector = [0] * split_index 
		result_matrix_00 = [[0 for x in range(split_index)] for y in range(split_index)] 
		result_matrix_01 = [[0 for x in range(split_index)] for y in range(split_index)] 
		result_matrix_10 = [[0 for x in range(split_index)] for y in range(split_index)] 
		result_matrix_11 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a00 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a01 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a10 = [[0 for x in range(split_index)] for y in range(split_index)] 
		a11 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b00 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b01 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b10 = [[0 for x in range(split_index)] for y in range(split_index)] 
		b11 = [[0 for x in range(split_index)] for y in range(split_index)] 

		for i in range(split_index): 
			for j in range(split_index): 
				a00[i][j] = matrix_A[i][j] 
				a01[i][j] = matrix_A[i][j + split_index] 
				a10[i][j] = matrix_A[split_index + i][j] 
				a11[i][j] = matrix_A[i + split_index][j + split_index] 
				b00[i][j] = matrix_B[i][j] 
				b01[i][j] = matrix_B[i][j + split_index] 
				b10[i][j] = matrix_B[split_index + i][j] 
				b11[i][j] = matrix_B[i + split_index][j + split_index] 

		add_matrix(multiply_matrix(a00, b00),multiply_matrix(a01, b10),result_matrix_00, split_index)
		add_matrix(multiply_matrix(a00, b01),multiply_matrix(a01, b11),result_matrix_01, split_index)
		add_matrix(multiply_matrix(a10, b00),multiply_matrix(a11, b10),result_matrix_10, split_index)
		add_matrix(multiply_matrix(a10, b01),multiply_matrix(a11, b11),result_matrix_11, split_index)

		for i in range(split_index): 
			for j in range(split_index): 
				result_matrix[i][j] = result_matrix_00[i][j] 
				result_matrix[i][j + split_index] = result_matrix_01[i][j] 
				result_matrix[split_index + i][j] = result_matrix_10[i][j] 
				result_matrix[i + split_index][j + split_index] = result_matrix_11[i][j] 

	return result_matrix 

# Driver Code
def main():
    
    banner()

    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    # Initialize matrix
    matrix_A = []
    matrix_A = populate(matrix_A, R, C)

    matrix_B = []
    matrix_B = populate(matrix_B, R, C)

    print_matrix(matrix_A, "Matrix A")
    print_matrix(matrix_B, "Matrix B") 

    start = time.time()
    result_matrix = multiply_matrix(matrix_A, matrix_B) 
    end = time.time()

    print_matrix(result_matrix, "Result Matrix")
    print("Time took by stressen multiplication method for {}x{}: {:.8f} seconds".format(R, C, end - start))


if __name__ == "__main__":
    main()
