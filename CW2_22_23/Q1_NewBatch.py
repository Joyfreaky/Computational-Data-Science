# For this question numpy and regex can be used if needed
import re
#import numpy as np

def shift_vowel(s):
    """"it takes as input a string s representing a word, sentence, or
paragraph. Your task is to shift the vowels by two positions contained in the string, where vowels are
the symbols a e i o u (and their capitalised versions A E I O U)"""
    # find the vowels
    vowels = re.findall(r"[aeiouAEIOU]", s)
    # shift the vowels
    shifted_vowels = []
    for vowel in vowels:
        shifted_vowels.append(chr(ord(vowel) + 2))

    # replace the vowels in the string
    for i in range(len(vowels)):
        s = s.replace(vowels[i], shifted_vowels[i])
    # print the result
    print("The vowels are " + "".join(vowels))
    print("The shifted vowels are " + "".join(shifted_vowels))
    print("The shifted string is " + s)
    # return the shifted string
    return s
    

    




def sum_of_digits(s):
    """It takes as input a string s that contains some numbers. The
function calculates the sum of all the digits in the string, ignoring any symbols that are not digits."""
    # spilt the digits and non-digits
    digits = re.findall(r"\d", s)
    non_digits = re.findall(r"[^\d]", s)
    # calculate the sum of digits
    sum = 0
    for digit in digits:
        sum += int(digit)
    # print the sum of digits
    print("The sum of digits operation performs " + "+".join(digits))
    print("The sum of digits is " + str(sum))
    # print the non-digits
    print("The non-digits are " + "".join(non_digits))
    # return the sum of digits
    return sum  





# To test your functions above, run the code below and compare your results with the example outputs below.
# Q1 Test Cases
if __name__ == '__main__':
    testcases = {'shift_vowel': ["a cat", "kite", "mood", "Oops"],
                 'sum_of_digits':[("123",), ("10a20b",), ("united",), ("",)]}

    print('\n-- Q1a testcases --')
    for args in testcases['shift_vowel']:
        print('input:', str(args))
        print('output:', shift_vowel(args))
        print('-----------')
    print('\n-- Q1b testcases --')
    for args in testcases['sum_of_digits']:
        print('input:', str(args))
        print('output:', sum_of_digits(*args))
        print('-----------')

# Expected Outputs
#-- Q1a testcases --
#input: a cat
#output: i cit
#-----------
#input: kite
#output: kuto
#-----------
#input: mood
#output: meed
#-----------
#input: Oops
#output: Eeps
#-----------
#
#-- Q1b testcases --
#input: ('123',)
#The sum of digits operation performs 1+2+3
#The extracted non-digits are:  []
#output: 6
#-----------
#input: ('we10a20b',)
#The sum of digits operation performs 1+0+2+0
#The extracted non-digits are:  ['w', 'e', 'a', 'b']
#output: 3
#-----------
#input: ('united',)
#The sum of digits operation could not detect a digit!
#The returned input letters are:  ['u', 'n', 'i', 't', 'e', 'd']
#output: 0
#-----------
#input: ('',)
#Empty string entered!
#output: 0
#-----------