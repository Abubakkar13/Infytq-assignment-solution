#OOPR-Assgn-29
#Start writing your code here
from abc import ABCMeta, abstractmethod

class Customer(metaclass = ABCMeta):
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None
        
    @abstractmethod
    def calculate_bill_amount(self):
        pass
    
    def get_customer_name(self):
        return self.__customer_name
        
    
class OccasionalCustomer(Customer):
    __counter = 1000
    def __init__(self, customer_name, distance_in_kms):
        super().__init__(customer_name)
        self.__distance_in_kms = distance_in_kms
        OccasionalCustomer.__counter += 1 
        self.bill_id = 'O' + str(OccasionalCustomer.__counter)
        
    def validate_distance_in_kms(self):
        return self.__distance_in_kms in range(1,6)
    
    def calculate_bill_amount(self):
        bill_amount = -1
        
        if self.validate_distance_in_kms():
            cost_per_tiffin = 50
           
            if self.__distance_in_kms <= 2 :
                delivery_charge = 5 * self.__distance_in_kms
            else:
                delivery_charge = 7.5 * self.__distance_in_kms
            
            bill_amount = cost_per_tiffin + delivery_charge
            
        self.bill_amount = bill_amount
        return bill_amount

    def get_distance_in_kms(self):
        return self.__distance_in_kms

        
class RegularCustomer(Customer):
    __counter = 100 
    def __init__(self, customer_name, no_of_tiffin):
        super().__init__(customer_name)
        self.__no_of_tiffin = no_of_tiffin
        RegularCustomer.__counter += 1 
        self.bill_id = "R" + str(RegularCustomer.__counter)
        
    def validate_no_of_tiffin(self):
        return self.__no_of_tiffin in range(1,8)
    
    def calculate_bill_amount(self):
        bill_amount = -1 
        if self.validate_no_of_tiffin():
            cost_per_tiffin = 50 
            no_of_days = 7
            bill_amount = cost_per_tiffin * self.__no_of_tiffin * no_of_days
        self.bill_amount = bill_amount
        return bill_amount
    
    def get_no_of_tiffin(self):
        return self.__no_of_tiffin
        
oc = OccasionalCustomer("Tony Stark", 3)
print("Name:", oc.get_customer_name())
print("Bill ID:", oc.bill_id)
print("Bill amount:", oc.calculate_bill_amount())
print("-----------------------------------------------------")

rc = RegularCustomer("John Wick", 2)
print("Name:", rc.get_customer_name())
print("Bill ID:", rc.bill_id)
print("Bill amount:", rc.calculate_bill_amount())
print("-----------------------------------------------------")

        
