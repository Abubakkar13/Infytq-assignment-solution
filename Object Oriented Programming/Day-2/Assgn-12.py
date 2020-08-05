#OOPR-Assgn-12
#Start writing your code here
class Bill:
    def __init__(self, bill_id, patient_name):
        self.__patient_name = patient_name
        self.__bill_id = bill_id
        self.__bill_amount = None
        
    def get_patient_name(self):
        return self.__patient_name
    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount
        
    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        total_bill_amt = 0
        for quantity,price in zip(quantity_list, price_list):
            total_bill_amt += quantity * price 
        total_bill_amt += consultation_fees
        self.__bill_amount = total_bill_amt

obj = Bill(1001, "John Wick")
obj.calculate_bill_amount(100, [2, 3, 5], [20, 25, 10])
print(obj.get_patient_name())
print(obj.get_bill_id())
print(obj.get_bill_amount())
