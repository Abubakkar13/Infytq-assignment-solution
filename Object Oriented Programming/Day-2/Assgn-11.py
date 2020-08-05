#OOPR-Assgn-11
#Start writing your code here
class Flower:
    
    def __init__(self):
        self.__flower_name = None
        self.__price_per_kg = None
        self.__stock_available = None
        
    def set_flower_name(self, flower_name):
        self.__flower_name = flower_name.lower()
    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg = price_per_kg
    def set_stock_available(self, stock_available):
        self.__stock_available = stock_available
        
    def get_flower_name(self): return self.__flower_name
    def get_price_per_kg(self): return self.__price_per_kg
    def get_stock_available(self): return self.__stock_available
    
    def validate_flower(self):
        return self.get_flower_name() in ['orchid', 'rose', 'jasmine']
        
    def check_level(self):
        if self.validate_flower():
            stock_available = self.get_stock_available()
            flower_name = self.get_flower_name()
            temp_dict={
                'orchid':15,
                'rose':25,
                'jasmine':40
                }
            level = temp_dict[flower_name]
            return stock_available < level
        return False
        
        
    def validate_stock(self, required_quantity):
        return required_quantity <= self.get_stock_available()
        
    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            stock = self.get_stock_available() - required_quantity
            self.set_stock_available(stock)
        return False 
        
obj = Flower()
obj.set_flower_name("Jasmine")
obj.set_price_per_kg(25)
obj.set_stock_available(30)
obj.sell_flower(20)
