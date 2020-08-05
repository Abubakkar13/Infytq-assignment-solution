'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of circular primes less than the given limit.
'''
#PF-Assgn-57
def check_prime(number):
     #remove pass and write your logic here. if the number is prime return true, else return false
    for i in range(2, number//2 + 1):
        if number %i == 0:
            return False
    return True

def rotations(num):
     #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    rotations_list = [num]
    while True:
        num = str(num)[1:] + str(num)[0]
        if int(num) not in rotations_list:
            rotations_list.append(int(num))
        else: break
    return rotations_list
    
def get_circular_prime_count(limit):
     #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
     count = 0 
     for i in range(2, limit):
         rotations_list = rotations(i)
         flag = True
         for j in rotations_list:
             if check_prime(j):
                 continue
             else:
                 flag = False
                 break
         if flag:
             count += 1 
     return count

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
