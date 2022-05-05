# CMT309 - 2021-2022 Coursework Q3 Test Code
# Oktay Karakus, PhD
# ************************************************************************************
def function_renamer():
    '''
    1) Please copy and pass your codes for function_renamer() function below.
    2) Do required changes in function definition for the arguments if needed.
    '''
    pass


### --- IMPORTANT: DO NOT REMOVE OR CHANGE THE CODE BELOW ---
if __name__ == '__main__':
    # Example 1
    testcases = {
        'example 1':
"""
def add_two_numbers(a, b):
  return a + b

print(add_two_numbers(10, 20))
""",
    'example 2' :
"""
def _major_split(*args):
  return (args[:2], args[2:])

def CheckTruth(t = True):
  print('t is', t)
  return _major_split([t]*10)

x, y = _major_split((10, 20, 30, 40, 50))
CheckTruth(len(x) == 10)
"""
    }
    for key, code in testcases.items():
        print(f'--- {key} ---')
        out = function_renamer(code)
        if not isinstance(out, tuple) or len(out)!=2:
            raise TypeError('function_renamer should return a tuple of length 2')
        d, newcode = out
        if not isinstance(d, dict):
            raise TypeError('return argument d should be a dictionary')
        if not isinstance(newcode, str):
            raise TypeError('return argument code should be a string')
        print('d = ', d)
        print('\ncode:')
        print(newcode)
        
### --- The outputs of test cases are given below. Please compare with your results.
# ************************************************************************************
# --- example 1 ---
# d =  {'add_two_numbers': {'hash': -8350170554082315684, 'camelcase': 'AddTwoNumbers', 'allcaps': 'ADD_TWO_NUMBERS'}}
# 
# code:
# 
# def AddTwoNumbers(a, b):
#   return a + b
# 
# print(AddTwoNumbers(10, 20))
# 
# --- example 2 ---
# d =  {'_major_split': {'hash': 5876647843514767306, 'camelcase': '_MajorSplit', 'allcaps': '_MAJOR_SPLIT'}, 'CheckTruth': {'hash': -8834367599083649426, 'camelcase': 'CheckTruth', 'allcaps': 'CHECKTRUTH'}}
# 
# code:
# 
# def _MajorSplit(*args):
#   return (args[:2], args[2:])
# 
# def CheckTruth(t = True):
#   print('t is', t)
#   return _MajorSplit([t]*10)
# 
# x, y = _MajorSplit((10, 20, 30, 40, 50))
# CheckTruth(len(x) == 10)