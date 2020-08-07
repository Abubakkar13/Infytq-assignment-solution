#OOPR-Assgn-32
#Start writing your code here
from abc import ABCMeta, abstractmethod
class Employee(metaclass = ABCMeta):
    def __init__(self, job_band, employee_name, basic_salary, qualification):
        self.__job_band = job_band
        self.__basic_salary = basic_salary
        self.__employee_name = employee_name
        self.__qualification = qualification
    
    @abstractmethod    
    def validate_job_band(self):
        pass
    def validate_basic_salary(self):
        return self.__basic_salary > 3000
    def validate_qualification(self):
        return self.__qualification in ["Bachelors", "Masters"]
    
    @abstractmethod
    def calculate_gross_salary(self):
        pass
    
    def get_job_band(self):
        return self.__job_band
    def get_employee_name(self):
        return self.__employee_name
    def get_qualification(self):
        return self.__qualification
    def get_basic_salary(self):
        return self.__basic_salary
        
class Graduate(Employee):
    def __init__(self, job_band, employee_name, basic_salary, qualification, cgpa):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa = cgpa
        
    def get_cgpa(self):
        return self.__cgpa
        
    def validate_job_band(self):
        return self.get_job_band() in ["A", "B", "C"]
        
    def calculate_gross_salary(self):
        if self.validate_job_band() and self.validate_qualification() and self.validate_basic_salary():
            gross_salary = self.get_basic_salary() 
            basic_salary = self.get_basic_salary()
            # Add PF - provident fund
            gross_salary += basic_salary * 0.12 
            # Add TPI amount
            if self.__cgpa >= 4.0 and self.__cgpa <= 4.25:
                gross_salary += 1000
            elif self.__cgpa <= 4.50:
                gross_salary += 1700
            elif self.__cgpa <= 4.75:
                gross_salary += 3200
            elif self.__cgpa <= 5.0:
                gross_salary += 5000
                
            # Add Incentive base on job band
            job_band = self.get_job_band()
            if job_band == "A":
                gross_salary += basic_salary * 0.04
            elif job_band == "B":
                gross_salary += basic_salary * 0.06
            else:
                gross_salary += basic_salary * 0.1 
            
            return gross_salary
        else:
            return -1
    
class Lateral(Employee):
    def __init__(self, job_band, employee_name, basic_salary, qualification, skill_set):
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set = skill_set
        
    def get_skill_set(self):
        return self.__Skill_set
    def validate_job_band(self):
        return self.get_job_band() in ["D", "E", "F"]
        
    def calculate_gross_salary(self):
        if self.validate_job_band() and self.validate_qualification() and self.validate_basic_salary():
            gross_salary = self.get_basic_salary() 
            basic_salary = self.get_basic_salary()
            # Add PF amount
            gross_salary += basic_salary * 0.12 
            # Add SME 
            if self.__skill_set == "AGP":
                gross_salary += 6500
            elif self.__skill_set == "AGPT":
                gross_salary += 8200
            elif self.__skill_set == "AGDEV":
                gross_salary += 11500
                
            # Add Incentive
            job_band = self.get_job_band()
            if job_band == "D":
                gross_salary += basic_salary * 0.13
            elif job_band == "E":
                gross_salary += basic_salary * 0.16
            else:
                gross_salary += basic_salary * 0.2 
            
            return gross_salary
        else:
            return -1

g = Graduate("A", "Tony Stank", 3500, "Masters", 4.5)
print("Graduate:")
print("Gross Salary:",g.calculate_gross_salary())
print()
l = Lateral("D", "Steve Rogers", 6500, "Masters", "AGP")
print("Lateral:")
print("Gross Salary:",l.calculate_gross_salary())
    
        
    
        
    
