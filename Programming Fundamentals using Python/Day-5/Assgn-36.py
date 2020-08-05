#PF-Assgn-36
def create_largest_number(number_list):
    #remove pass and write your logic here
    new_list = [str(num) for num in reversed(sorted(number_list))]
    return int(''.join(new_list))

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
