#PF-Assgn-38

def check_double(number):
    #Remove pass and write your logic here
    num1 = str(number)
    num2 = str(number * 2)
    if not(len(num1) == len(num2)):
        return False
    for i in range(len(num1)):
        if num1[i] not in num2:
            return False
        elif num1[i] == num2[i]:
            return False
    return True

#Provide different values for number and test your program
print(check_double(125874))
