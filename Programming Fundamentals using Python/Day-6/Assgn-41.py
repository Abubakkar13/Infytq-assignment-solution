'''
A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str)
which accepts a string and returns the list of 10-substrings of that string.
'''

#PF-Assgn-41
def find_ten_substring(num_str):
    result_list = list()
    for i in range(len(num_str)):
        sm = int(num_str[i]) 
        temp_str = num_str[i]
        for j in range(i+1, len(num_str)):
            if sm > 10:
                break
    
            else:
                sm += int(num_str[j])
                temp_str += num_str[j]
                
                if sm == 10:
                    result_list.append(temp_str)
    #Remove pass and write your logic here
    return result_list

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
