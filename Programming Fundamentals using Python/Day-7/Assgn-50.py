#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    data = data.split()
    result = list()
    for word in data:
        for i in word:
            flag = False 
            if i not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                flag = True 
                break
        if flag:
            temp = ''
            for i in word:
                if i not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                    temp += i 
            result.append(temp)
        else:
            result.append(word)
    return ' '.join(result)  

data="I love Python"
print(sms_encoding(data))
