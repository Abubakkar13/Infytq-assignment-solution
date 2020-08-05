#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    if num1 < num2:
        for num in range(num1, num2+1):
            # a. Sum of the digits of the number is a multiple of 3 i.e. check if number is multiple of 3
            # b. Number has only two digits
            # c. Number is a multiple of 5
            
            if (num % 3 == 0) and (num % 5 == 0) and (num // 100 == 0):
                max_num = num 
            
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
