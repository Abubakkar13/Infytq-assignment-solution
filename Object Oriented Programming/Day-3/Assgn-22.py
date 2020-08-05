#OOPR-Assgn-22
class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        '''Write the logic to book the given number of tickets for the specified movie.'''
        if movie_name not in Multiplex.__list_movie_name:
            return 0 
            
        movie_index = Multiplex.__list_movie_name.index(movie_name)
        if not self.check_seat_availability(movie_index, number_of_tickets):
            return -1 
        else:
            list_of_seat_numbers = self.generate_seat_number(movie_index, number_of_tickets)
            
            self.__seat_numbers = list_of_seat_numbers
            self.calculate_ticket_price(movie_index, number_of_tickets)
            
    def  generate_seat_number(self,movie_index, number_of_tickets):
        '''Write the logic to generate and return the list of seat numbers'''
        temp_str = "M" + str(movie_index+1) + '-'
        temp_list = []
        if Multiplex.__list_last_seat_number[movie_index] == None:
            for i in range(1, number_of_tickets+1):
                temp_list.append(temp_str + str(i))
            
        else:
            start_index = int(Multiplex.__list_last_seat_number[movie_index].split('-')[-1]) + 1
             
            for i in range(start_index, start_index + number_of_tickets):
                temp_list.append(temp_str + str(i))
                
        Multiplex.__list_last_seat_number[movie_index] = temp_list[-1]
        Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
        
        return temp_list
        
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())
