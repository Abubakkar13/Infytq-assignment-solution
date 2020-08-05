#PF-Assgn-44

def find_duplicates(list_of_numbers):
    #start writing your code here
    result_list = list() #  list of duplicates
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] in list_of_numbers[i+1:]:
            result_list.append(list_of_numbers[i])
    return result_list

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
