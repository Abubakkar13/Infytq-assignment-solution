#OOPR-Assgn-7
#Start writing your code here
class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__technology_skill = None
        self.__experience = None
        self.__avg_feedback = None
        
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name
    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill
    def set_experience(self, experience):
        self.__experience = experience
    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback
        
    def get_instructor_name(self):
        return self.__instructor_name
    def get_technology_skill(self):
        return self.__technology_skill
    def get_experience(self):
        return self.__experience
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def check_eligibility(self):
        if self.__experience > 3:
            return self.__avg_feedback >= 4.5
        else:
            return self.__avg_feedback >= 4.0
        
    def allocate_course(self, technology):
        if self.check_eligibility():
             return technology in self.__technology_skill
        else: return False
inst = Instructor()
inst.set_instructor_name("Monty")
inst.set_experience(5.0)
inst.set_technology_skill(["Python", "C++", "Java"])
inst.set_avg_feedback(4.6)
print(inst.allocate_course("Python"))

