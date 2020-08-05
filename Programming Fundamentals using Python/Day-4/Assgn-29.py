#PF-Assgn-29
def calculate(distance,no_of_passengers):
    litre = distance / 10 
    actual_cost = litre * 70
    earned_cost = no_of_passengers * 80
    if earned_cost >= actual_cost:
        return earned_cost - actual_cost
    else: 
        return -1
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
