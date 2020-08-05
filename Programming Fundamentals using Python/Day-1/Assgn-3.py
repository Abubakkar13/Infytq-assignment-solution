#PF-Assgn-3
#This verification is based on string match.

mileage=12
amount_per_litre=65
distance_one_way=96
per_head_cost=0
divisible_by_five=False

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
total_litre = distance_one_way // mileage
total_cost = (amount_per_litre * total_litre) * 2 
per_head_cost = total_cost // 4
if per_head_cost % 5 == 0:
    divisible_by_five = True

#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
