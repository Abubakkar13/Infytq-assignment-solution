'''    Recursive Palindrome '''

#PF-Assgn-40
def is_palindrome(word):
    if len(word) == 1 or len(word) == 0 : return True
    elif word[0] != word[-1]: return False
    else:
        return is_palindrome(word[1:len(word)-1])
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("abcddcba")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
