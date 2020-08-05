#PF-Assgn-58

def validate_credit_card_number(card_number):
    #start writing your code here
    card_number = str(card_number)
    temp_list1 = [int(card_number[i])*2 for i in range(0, len(card_number), 2)]
    
    temp_list2 = [int(card_number[i]) for i in range(1, len(card_number), 2)]
    
    for i in range(len(temp_list1)):
        if i > 9:
            sm = sum(map(int, list(str(i))))
            temp_list1[i] = sm
    total = sum(temp_list1) + sum(temp_list2)
    return total % 10 == 0 
        
            
card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
