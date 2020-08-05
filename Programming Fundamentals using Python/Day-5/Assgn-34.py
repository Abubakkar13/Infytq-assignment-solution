#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    #Remove pass and write your logic here
    pair_list = list()
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if i + j == n : 
                pair_list.append((i, j))
    return len(pair_list)

num_list=[1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))
