#OOPR-Assgn-16

class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phone_no,called_no,duration):
        self.phone_no=phone_no
        self.called_no=called_no
        self.duration=duration

class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects = None
        
    def parse_customer(self,list_of_customers,list_of_calls):
        self.list_of_customer_calldetail_objects = list_of_calls
        for cust in list_of_customers:
            temp_list = list()
            for call in list_of_calls:
                if cust.phone_no == call.phone_no:
                    temp_list.append(call)
            cust.list_of_calls = temp_list
        
list_of_customers=[Customer(age=23 , phone_no=9900009901 , name="cust1"), Customer(age=24 , phone_no=9900009902 , name="cust2"), Customer(age=25 , phone_no=9900009966 , name="cust3")]


list_of_calls=[CallDetail(duration=5 , called_no=8800123401 , phone_no=9900009901), CallDetail(duration=10 , called_no=8800123402 , phone_no=900009903), CallDetail(duration=2 , called_no=8800123403 , phone_no=9900009902), CallDetail(duration=8 , called_no=8800123404 , phone_no=9900009901), CallDetail(duration=7 , called_no=8800123405 , phone_no=9900009901), CallDetail(duration=9 , called_no=8800123406 , phone_no=9900009909), CallDetail(duration=4 , called_no=8800123407 , phone_no=9900009903)]

Util().parse_customer(list_of_customers, list_of_calls)
