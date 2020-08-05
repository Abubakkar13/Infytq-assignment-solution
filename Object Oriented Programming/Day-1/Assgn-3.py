#OOPR-Assgn-3
#Start writing your code here
class Customer:
    def __init__(self):
        self.customer_name = None
        self.bill_amount = None
    
    def purchases(self):
        discount = 0.05 
        if self.bill_amount != None:
            self.bill_amount -= self.bill_amount * discount 
        
    
    def pays_bill(self, amount):
        print(self.customer_name,"pays bill amount of Rs.",self.bill_amount)

jill = Customer()
jill.customer_name = "Jill"
jill.bill_amount = 50000
jill.purchases()
jill.pays_bill(50000)
