#PF-Assgn-60
def remove_duplicates(value):
    #start writing your code here
    result = ""
    for i in range(len(value)):
        if value[i] not in result:
            result += value[i] 
    return result

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
