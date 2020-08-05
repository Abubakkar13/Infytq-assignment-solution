'''
Write a python program to help an airport manager to generate few statistics based on the ticket details available for a day.

Go through the below program and complete it based on the comments mentioned in it.


Note: Perform case sensitive string comparisons wherever necessary.
'''
#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=['AI101:MUM:LON:001', 'AI101:MUM:LON:002', 'SI456:MUM:SIN:145', 'EM456:MUM:DUB:098', 'SI456:MUM:SIN:050', 'SI456:MUM:SIN:051']

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2] == destination):
            count+=1
    return count
    #Remove pass and write your logic here

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    temp_dict = dict()
    for i in ticket_list:
        string_list = i.split(':')
        if string_list[0] in temp_dict:
            temp_dict[string_list[0]] += 1 
        else:
            temp_dict.update({string_list[0]:1})
    result = list()
    for key,value in temp_dict.items():
        result.append(key+':'+str(value))
    return result
    #Remove pass and write your logic here

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    temp_list = find_passengers_per_flight()
    for i in range(len(temp_list)):
        string_list = temp_list[i].split(':')
        temp_list[i] = string_list[1] + ':' + string_list[0]
    sorted_list = sorted(temp_list, reverse=True)
    for i in range(len(sorted_list)):
        string_list = sorted_list[i].split(':')
        sorted_list[i] = string_list[1] + ':' + string_list[0]
    return sorted_list
    #Remove pass and write your logic here

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
