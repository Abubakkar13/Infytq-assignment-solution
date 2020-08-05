'''
Write a python function, check_anagram() which accepts two strings and returns
True, if one string is an anagram of another string. Otherwise returns False.

The two strings are considered to be an anagram if they contain repeating
characters but none of the characters repeat at the same position.

The length of the strings should be the same.

Also write the pytest test cases to test the program.

    Sample Input	Expected Output
    eat, tea	             True    (Reason: character 'a' repeats at position 6, not an anagram)
    backward,drawback	     False
                                  
    Reductions,discounter    True
    About, table	     False
'''
#PF-Assgn-54
def check_anagram(data1,data2):
    n = len(data1)
    for i in range(n):
        if data1[i] != data2[i] and data1[i] in data2:
            continue
        else:
            return False
    return True

print(check_anagram("eat","tea"))
