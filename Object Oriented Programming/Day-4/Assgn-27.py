#OOPR-Assgn-27
#This class represents ThemePark
class ThemePark:

    dict_of_games={"Game1":[35.5,5], "Game2":[40.0,6],"Game3":[120.0,10], "Game4":[60.0,7],"Game5":[25.0,4]}
    
    @staticmethod
    def validate_game(game_input):
        return game_input in ThemePark.dict_of_games

    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games[game_input][1]

    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games[game_input][0]

class Ticket:
    __ticket_count=200
    def __init__(self):
        self.__ticket_id=None
        self.__ticket_amount=0
    
    def generate_ticket_id(self):
        Ticket.__ticket_count += 1 
        self.__ticket_id = Ticket.__ticket_count

    def calculate_amount(self, list_of_games):
        total_amt = 0 
        for game in list_of_games:
            if ThemePark.validate_game(game):
                total_amt += ThemePark.get_amount(game)
            else:
                return False
        self.__ticket_amount = total_amt
        return True
        
    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer:
    def __init__(self, name, list_of_games):
        self.__name = name
        self.__list_of_games = list_of_games
        self.__ticket = Ticket()
        self.__points_earned = 0
        self.__food_coupon = "No"
        
    def get_name(self):
        return self.__name
    def get_list_of_games(self):
        return self.__list_of_games
    def get_food_coupon(self):
        return self.__food_coupon
    def get_ticket(self):
        return self.__ticket
    def get_points_earned(self):
        return self.__points_earned
        
    def update_food_coupon(self):
        if ("Game4" in self.__list_of_games) and (self.__points_earned > 15):
            self.__food_coupon = "Yes"
    
    def play_game(self):
        total_points = 0 
        for game in self.__list_of_games:
            if ThemePark.validate_game(game):
                total_points += ThemePark.get_points(game)
        if 'Game3' in self.__list_of_games:
            self.__list_of_games.append('Game2')
            total_points += ThemePark.get_points("Game2")
        self.__points_earned = total_points
    
    def book_ticket(self):
        amt = self.__ticket.calculate_amount(self.__list_of_games)
        if amt:
            self.__ticket.generate_ticket_id()
            self.play_game()
            self.update_food_coupon()
            return True
        return False

cust = Customer("John Wick", ['Game2', 'Game1', 'Game4'])
if cust.book_ticket():
    print("Name:", cust.get_name())
    print("List of games:", cust.get_list_of_games())
    print("Ticket ID:", cust.get_ticket().get_ticket_id())
    print("Ticket amount:", cust.get_ticket().get_ticket_amount())
    print("Points earned:", cust.get_points_earned())
    print("Food coupon:", cust.get_food_coupon())
else:
    print("Some Error Occured")
