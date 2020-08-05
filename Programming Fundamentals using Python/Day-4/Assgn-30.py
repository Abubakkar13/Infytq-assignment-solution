#PF-Assgn-30

def encode(message):
    count = 1 
    new_message = ''
    if len(message) == 1:
        return str(1) + message
    for i in range(len(message) - 1):
        if message[i] == message[i+1]:
             count += 1 
             continue
        new_message += str(count) + message[i]
        count = 1  
    if len(message) >= 2 and message[-2] != message[-1]:
        new_message += str(1) + message[-1]
    return new_message
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
