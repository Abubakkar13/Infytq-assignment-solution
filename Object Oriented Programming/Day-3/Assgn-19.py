#OOPR-Assgn-19
class Ticket:
    counter = 00
    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination
        self.__ticket_id = None
        
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def get_ticket_id(self):
        return self.__ticket_id
        
    def validate_source_destination(self):
        return self.__source.lower() == "delhi" and self.__destination.lower() in ("mumbai", "pune", "kolkata", "chennai")
    
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            if Ticket.counter<10:
                ticket_id = "D" + self.__destination.capitalize()[0] + "0" + str(Ticket.counter)
            else:
                ticket_id = "D" + self.__destination.capitalize()[0] + str(Ticket.counter)
            self.__ticket_id = ticket_id 
        
    
passenger = Ticket("John Wick", "delhi", "Kolkata")
passenger.generate_ticket()
print("Name: ", passenger.get_passenger_name())
print("Ticket ID: ", passenger.get_ticket_id())
print("Source: ", passenger.get_source())
print("Destination: ", passenger.get_destination())
print("-----------------------------------------------------")
print()
