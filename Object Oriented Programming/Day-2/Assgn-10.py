#OOPR-Assgn-10

class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.__phoneno = phoneno
        self.__called_no = called_no
        self.__duration = duration
        self.__call_type = call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        call_list = []
        for call_details in list_of_call_string:
            call_details = call_details.split(',')
            call_list.append(CallDetail(call_details[0],call_details[1],call_details[2],call_details[3]))
        self.list_of_call_objects = call_list

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
