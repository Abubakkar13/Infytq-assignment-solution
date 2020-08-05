#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    return sum(chocolates_received)
    #Remove pass and write your logic here to find and return the total number of chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    if child_id_rewarded not in child_id:
        print("Child id is invalid")
    elif extra_chocolates < 1:
        print("Extra chocolates is less than 1") 
    else:
        for id in range(len(child_id)):
            if child_id[id] == child_id_rewarded:
                chocolates_received[id] += extra_chocolates
        print(chocolates_received)

    #Remove pass and write your logic here


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #
    
    

print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)
