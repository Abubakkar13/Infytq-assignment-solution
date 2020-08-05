'''
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
Also write the pytest test cases to test the program.


'''
#PF-Assgn-46
def nearest_palindrome(number):
    #start writitng your code here
    while True:
        number += 1
        word = str(number)
        if word == word[::-1]:
            return number
        

number=12300
print(nearest_palindrome(number))
