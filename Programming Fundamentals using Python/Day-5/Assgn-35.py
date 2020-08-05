#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    avg = sum(list_of_marks) / len(list_of_marks)
    more_than_avg = [i for i in list_of_marks if i > avg]
    return len(more_than_avg) / len(list_of_marks) * 100
    #Remove pass and write your logic here

def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here

def generate_frequency():
    freq_list = [0 for _ in range(26)]
    for mark in list_of_marks:
        freq_list[mark] += 1 
    return freq_list
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
