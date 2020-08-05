#OOPR-Assgn-17
#Start writing your code here
class Customer:
    def __init__(self, customer_id, customer_name, address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__address = address
        
    def get_customer_name(self):
        return self.__customer_name
    def get_customer_id(self):
        return self.__customer_id
    def get_address(self):
        return self.__address
    
    def validate_customer_id(self):
        customer_id = str(self.get_customer_id())
        return len(customer_id) == 6 and customer_id[0] == "1"
        
class Freight:
    counter = 198
    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__recipient_customer = recipient_customer
        self.__from_customer = from_customer
        self.__weight = weight
        self.__distance = distance
        self.__freight_id = None
        self.__freight_charge = None
        
    def get_recipient_customer(self): return self.__recipient_customer
    def get_from_customer(self): return self.__from_customer
    def get_weight(self): return self.__weight
    def get_distance(self): return self.__distance
    def get_freight_id(self): return self.__weight
    def get_freight_charge(self): return self.__freight_charge
    
    def validate_weight(self):
        return self.get_weight() % 5 == 0
    def validate_distance(self):
        return self.get_distance() in range(500, 5001)
        
    def forward_cargo(self):
        
        if self.get_recipient_customer().validate_customer_id() and self.get_from_customer().validate_customer_id() and self.validate_distance() and self.validate_weight():
            
            Freight.counter += 2 
            self.__freight_id = Freight.counter
            
            weight_price = 150 * self.get_weight()
            dist_price = 60 * self.get_distance()
            total_price = weight_price + dist_price
            self.__freight_charge = total_price
        else:
            self.__freight_charge = 0 
            
cust1 = Customer(111101, "John Wick", "121 street")
cust2 = Customer(121503, "John Cena", "125 street")
freight = Freight(cust1, cust2, 20, 503)
freight.forward_cargo()
print("Customer 1:")
print("Name: ", cust1.get_customer_name())
print("ID: ", cust1.get_customer_id())
print("Address: ", cust1.get_address())
print()
print("Customer 2:")
print("Name: ", cust2.get_customer_name())
print("ID: ", cust2.get_customer_id())
print("Address: ", cust2.get_address())
print()
print("Freight ID: ", freight.get_freight_id())
print("Freight Charge: ", freight.get_freight_charge())
