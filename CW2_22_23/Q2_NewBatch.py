import numpy as np



def matrix_multiplication(*argv):
     """Multiplication of two or more matrices."""
     # check the shape of the input matrices
     if len(argv) == 2:
         if argv[0].shape[1] == argv[1].shape[0]:
          # explicit for loops
               res = np.zeros((len(argv[0]), len(argv[1][0])))
               for i in range(len(argv[0])):
                    for j in range(len(argv[1][0])):
                         for k in range(len(argv[1])):
                              res[i][j] += argv[0][i][k] * argv[1][k][j]
               return res

         else:
             print("The shape of the input matrices is not suitable for matrix multiplication.")
             return None
     elif len(argv) > 2:
         if argv[0].shape[1] == argv[1].shape[0]:
             for i in range(2, len(argv)):
                 if argv[i-1].shape[1] == argv[i].shape[0]:
                     pass
                 else:
                     print("The shape of the input matrices is not suitable for matrix multiplication.")
                     return None
             
             res = np.matmul(argv[0], argv[1])
             for i in range(2, len(argv)):
                 res = np.matmul(res, argv[i])
             return res
         else:
             print("The shape of the input matrices is not suitable for matrix multiplication.")
             return None
     else:
         print("The number of input matrices is not suitable for matrix multiplication.")
         return None
     
     

def linear_solver(A, b):
     """While function argument A is a matrix, b is a column vector, 
     The function return the solution of variables in a variable res, which is a column vector as well.
     All of A, b and res should be numpy arrays
     • For the cases below, the function should return None and print a suitable message depending
on the case below.
For number of equations are lower than the variables, the system becomes an Underdetermined system, and this system has infinitely many solutions.
For number of equations are higher than the variables, the system becomes an Overdetermined system, and this system has no solution.
Other kinds of dimension mismatches.
• In cases when number of equations and variables are equal, the system has a unique solution
and can be found via the equation given above. This solution should be returned in variable
res, and the function should print a suitable message.
• For the matrix inverse, you are free to use np.linalg.inv() function.
• Matrix multiplication should be done by using the function, matrix_multiplication(), created
in the subsection above.
"""
     # check the shape of the input matrices
     if A.shape[0] == b.shape[0]:
         if A.shape[0] == A.shape[1]:
             # calculate the solution
             res = np.matmul(np.linalg.inv(A), b)
             # print the solution
             print("The Linear System has a unique solution:")
             # return the solution
             return res
         elif A.shape[0] > A.shape[1]:
             print("The system is Overdetermined, and has no solution.")
             return None
         else:
             print("The system is Underdetermined, and has infinitely many solutions.")
             return None
     else:
         print("The shape of the input matrices is not suitable for linear system.")
         return None

     


def LLS(A, b):
     # Find the Moore-Penrose pseudoinverse of a matrix A.
     A_plus =  matrix_multiplication

# To test your functions above, run the code below and compare your results with the example outputs below.
# Q2 Test Cases
if __name__ == '__main__':
    testcases = {'a': [(np.ones((2,3)), np.ones((3,2)))],
                 'b':[(np.array(range(6)).reshape((3,2)), np.ones((3,2))), 
                      (np.array([[3, 2, -1], [2, -2, 4], [0.5, -4, 1.5]]), np.array([[1], [3], [-7]]))],
                 'c':[(np.array([[3, -9, -1], [-2, -2, 14], [0.5, -12, 1.5]]),
                       np.array([[3], [-1], [0.5]]))],
                 'd':[(np.array([[3, -9, -1], [-2, -2, 14], [0.5, -12, 1.5]]),
                       np.array([[3], [-1], [0.5]]),
                       np.array([[1, 2, 3]]),)]}
          
    print('\n-- Q2a testcases --')
    for args in testcases['d']:
        print('input:', str(args))
        print('output:', matrix_multiplication(*args))
        print('-----------')
    print('\n-- Q2b testcases --')
    for args in testcases['b']:
        print('input:', str(args))
        print('output:', linear_solver(*args))
        print('-----------')
    """ print('\n-- Q2c testcases --')
    for args in testcases['c']:
        print('input:', str(args))
        print('output:', LLS(*args))
        print('-----------') """

# Example Test Outputs
#-- Q2a testcases --
#input: (array([[1., 1., 1.],
#       [1., 1., 1.]]), array([[1., 1.],
#       [1., 1.],
#       [1., 1.]]))
#output: [[3. 3.]
# [3. 3.]]
#-----------
#
#-- Q2b testcases --
#input: (array([[0, 1],
#       [2, 3],
#       [4, 5]]), array([[1., 1.],
#       [1., 1.],
#       [1., 1.]]))
#The Inputs are not suitable for a linear system of equations.
#output: None
#-----------
#input: (array([[ 3. ,  2. , -1. ],
#       [ 2. , -2. ,  4. ],
#       [ 0.5, -4. ,  1.5]]), array([[ 1],
#       [ 3],
#       [-7]]))
#Unique Solution!
#output: [[-0.59090909]
# [ 2.54545455]
# [ 2.31818182]]
#-----------
#
#-- Q2c testcases --
#input: (array([[  3. ,  -9. ,  -1. ],
#       [ -2. ,  -2. ,  14. ],
#       [  0.5, -12. ,   1.5]]), array([[ 3. ],
#       [-1. ],
#       [ 0.5]]))
#output: [[1.06710526]
# [0.01315789]
# [0.08289474]]
#-----------