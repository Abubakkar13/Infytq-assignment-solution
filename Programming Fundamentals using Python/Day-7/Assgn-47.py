'''
Write a python function, encrypt_sentence() which accepts a message and
encrypts it based on rules given below and returns the encrypted message.

Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants
                appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.
Also write the pytest test cases to test the program.

    Sample Input	             Expected Output
the sun rises in the east	eht snu sesir ni eht stea

'''
#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    sentence = sentence.split()
    result_list = list()
    for word in range(len(sentence)):
        if word % 2 == 0:
            result_list.append(sentence[word][::-1])
        else:
            temp_str1 = ''
            temp_str2 = ''
            for i in sentence[word]:
                if i in vowels:
                    temp_str2 += i 
                else:
                    temp_str1 += i 
            result_list.append(temp_str1 + temp_str2)
    return ' '.join(result_list)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
