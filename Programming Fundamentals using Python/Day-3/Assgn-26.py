#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    flag = False
    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    for i in range(0, heads+1):
        x, y = i, heads - i 
        head_test = x + y 
        leg_test = 2 * x + 4 * y  
        if head_test == heads and leg_test == legs:
            chicken_count = x 
            rabbit_count = y  
            flag = True
            break
    if flag:
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

#Provide different values for heads and legs and test your program
solve(38,131)
