#OOPR-Assgn-25
#Start writing your code here
class FruitInfo:
    __fruit_name_list = ["Apple","Guava","Orange","Grape", "Sweet Lime"] 
    __fruit_price_list =[200, 80, 70, 110, 60]
    
    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list
    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list
    @staticmethod
    def get_fruit_price(fruit_name):
        try:
            index = FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[index]
        except ValueError:
            return -1
        
class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type
        
    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type
        
class Purchase:
    __counter = 00
    def __init__(self, customer, fruit_name, quantity):
        self.__purchase_id = None
        self.__customer = customer
        self.__fruit_name = fruit_name 
        self.__quantity = quantity
        
    def get_customer(self):
        return self.__customer
        
    def get_purchase_id(self):
        return self.__purchase_id
        
    def get_quantity(self):
        return self.__quantity
        
    def calculate_price(self):
        fruit_price = FruitInfo.get_fruit_price(self.__fruit_name)
        
        if fruit_price != -1:
            total_price = fruit_price*self.__quantity
            mx = max(FruitInfo.get_fruit_price_list())
            mn = min(FruitInfo.get_fruit_price_list())
            if fruit_price == mx and self.__quantity>1:
                total_price -= total_price*0.02
            elif fruit_price == mn and self.__quantity>=5:
                total_price -= total_price*0.05
            
            if self.__customer.get_cust_type() == "wholesale":
                total_price -= total_price*0.1 
                
            self.__purchase_id = "P" + str(Purchase.__counter)
            Purchase.__counter += 1 
            return total_price
        return -1
        
cust = Customer("John Wick", "wholesale")
purchase = Purchase(cust, "Apple", 2)
print(purchase.calculate_price())
