#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    #Remove pass and write the logic here
    if filter_func == None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))

def even(data):
     #Remove pass and write the logic here
     return [num for num in data if num%2 == 0]

def odd(data):
     #Remove pass and write the logic here
     return [num for num in data if num%2 != 0]

sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))
