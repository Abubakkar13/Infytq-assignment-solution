#PF-Assgn-33

def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    common_characters = ''
    for char in msg1:
        if (char not in common_characters) and (char in msg2):
            common_characters += char 
    if len(common_characters) > 0:
        return common_characters
    else:
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
