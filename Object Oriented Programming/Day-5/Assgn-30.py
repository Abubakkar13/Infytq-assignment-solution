#OOPR-Assgn-30
#Start writing your code here
class Pizzaservice:
    counter = 100
    def __init__(self, customer, pizza_type="invalid", additional_topping=False):
        self.__service_id = None
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = -1
    
    def validate_pizza_type(self):
        return self.__pizza_type.lower() in ["small", "medium"]
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            # Calculate cost per pizza
            if self.__pizza_type.lower() == "small":
                pizza_cost = 150
                if self.__additional_topping:
                    pizza_cost += 35
            else:
                pizza_cost = 200
                if self.__additional_topping:
                    pizza_cost += 50 
            #Calculate price depending upon quantity
            pizza_cost *= self.__customer.get_quantity()
            self.pizza_cost = pizza_cost
            
            #Generate servie id
            Pizzaservice.counter += 1 
            self.__service_id = self.__pizza_type[0] +str(Pizzaservice.counter)
            
    
    def get_service_id(self):
        return self.__service_id
    def get_customer(self):
        return self.__customer
    def get_pizza_type(self):
        return self.__pizza_type
    def get_additional_topping(self):
        return self.__additional_topping
        
class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity
        
    def validate_quantity(self):
        return self.__quantity in range(1,6)
        
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
        
class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        self.__delivery_charge = 0 
        self.__distance_in_kms = distance_in_kms
        super().__init__(customer, pizza_type, additional_topping)
        
    def validate_distance_in_kms(self):
        return self.__distance_in_kms in range(1,11)
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                distance = 1 
                while distance <= self.__distance_in_kms:
                    if distance in range(1,6):
                        self.pizza_cost += 5 
                    elif distance in range(6,11):
                        self.pizza_cost += 7
                    distance += 1 
        else:
            self.pizza_cost = -1 
    
    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms
        
cust = Customer("John Wick", 1)
ps = Pizzaservice(cust, "Medium", True)
ps.calculate_pizza_cost()
print("Name:", cust.get_customer_name())
print("Quantity:", cust.get_quantity())
print("Pizza cost:", ps.pizza_cost)
print("Service ID:", ps.get_service_id())
print("-------------------------------------------------")
cust = Customer("Tony Stark", 3)
dd =Doordelivery(cust, "SMall", False, 10)
dd.calculate_pizza_cost()
print("Name:", cust.get_customer_name())
print("Quantity:", cust.get_quantity())
print("Pizza cost:", dd.pizza_cost)
print("Service ID:", dd.get_service_id())
print("-------------------------------------------------")

        
