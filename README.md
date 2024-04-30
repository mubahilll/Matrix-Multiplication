# Matrix Multiplication Algorithms
This repository contains Python implementations of two matrix multiplication algorithms: Naive Matrix Multiplication and Strassen's Matrix Multiplication.

## Naive Matrix Multiplication
The naive approach to matrix multiplication involves straightforward iteration through rows and columns, resulting in a time complexity of O(n^3) for two n x n matrices. This implementation utilizes the numpy.dot function for matrix multiplication.

## Strassen's Matrix Multiplication
Strassen's algorithm is a divide-and-conquer approach that reduces the number of multiplications required for matrix multiplication, resulting in a time complexity of approximately O(n^2.81). This implementation is specifically designed for square matrices.

### Usage
To use the naive matrix multiplication algorithm:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/mubahilll/Matrix-Multiplication
   ```
2. Navigate to the directory containing files.
   ```bash
   cd Matrix-Multiplication
   ```
3. Run the script using Python 3.
   ```bash
   python3 naive.py
   python3 strassen.py
   ```

Follow the prompts to input the number of rows and columns for the matrices

## Requirements
- Python3
- NumPy (for the naive matrix multiplication implementation)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
