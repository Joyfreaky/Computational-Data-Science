# CMT309 - CMT314 2021-2022 Coursework Q1
# Oktay Karakus, PhD
# *******************************************************************
def do_arithmetic():
    '''
    1) Please copy and pass your codes for do_arithmetic() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    '''
    1) Please copy and pass your codes for do_arithmetic() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    ''' This function performs an arthematic operation, namely: Addition, Subsraction, Multiplication and division,it takes two numbers as its arguement and the third argument is the type of operation and returns the computed value according to the type of operation
    '''
    if pd.isnull(x) or pd.isnull(y):
        return 'Please enter Valid Values'
    else:
        op1=op.lower()                                                 #Convert to lower case, in case of string.
        x=float(x)
        y=float(y)
    if op1=="add" or op1== "addition" or op1=="+" or op1 == '':        #Check and perform addition
        a= x + y
        return a
    elif op1=="subtract" or op1== "subtraction" or op1== "-":          #Check and perform substraction
        s= x - y
        return s
    elif op1=="multiply" or op1== "multiplication" or op1== "*":       #Check and perform multiplication
        m= x * y
        return m
    elif op1=="divide" or op1== "division" or op1=="/":                #Check and perform division
        if y==0:                                                       #Check if the division is by 0
            print("Division by 0!")
            return 'None'
        else:
            d= x / y
            return d
    else:                                                              # Check if the operation is not valid in the scope.
        return 'Unknown Arithematic Operation'

    
    pass

def sum_of_digits():
    '''
    1) Please copy and pass your codes for sum_of_digits() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    pass
