from prettytable import PrettyTable
import numpy as np 
import time
import random

def banner():
    CYAN = "\033[36m"
    font = f"""{CYAN}
            ** Naive Matrix Multiplication ** 
    -> Both matrices will have same number of rows and column
    -> Matrices are populated with random values\n"""
    print(font)

def populate(m, r, c):
    for i in range(r):       # A for loop for row entries
        a =[]
        for j in range(c):      # A for loop for column entries
            a.append(int(random.randrange(1,10)))
        m.append(a)
    return m   

def print_matrix(matrix, title="Matrix"):
    table = PrettyTable()
    table.title = title
    table.field_names = [f"Col {i+1}" for i in range(len(matrix[0]))]
    
    for row in matrix:
        table.add_row(row)

    print(table)

def main():
    banner()

    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    
    # Initialize matrix
    matrix_A = []
    matrix_A = populate(matrix_A, R, C)
    print_matrix(matrix_A, "Matrix A")

    matrix_B = []
    matrix_B = populate(matrix_B, R, C)
    print_matrix(matrix_B, "Matrix B")

    start = time.time()
    result = np.dot(matrix_A, matrix_B)
    end = time.time()

    print_matrix(result, "Result Matrix")
    print("Time took by naive multiplication method for {}x{}: {:.8f} seconds".format(R, C, end - start))

if __name__ == "__main__":
    main()