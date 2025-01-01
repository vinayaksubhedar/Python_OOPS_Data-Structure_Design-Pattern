"""Basics of Object Oriented Programming"""

class Email:
    pass

e1 = Email()



class Employee:
    '''Documentation String : This is Employee class'''

    no_of_students = 0
    gratuaty_percent = 8.5
    yearamount = 10000

    def __init__(self, name,gender,age, salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = 200000
        self.years = 5
        Employee.increamentempcount()

    @classmethod
    def increamentempcount(cls):
        cls.no_of_students = cls.no_of_students + 1

    @classmethod
    def getnoofstudents(cls):
        return cls.no_of_students

    def getname(self):
        return self.name
    
    def setname(self,name):
        self.name = name
    
    def getgender(self):
        return self.gender
    
    def setgender(self,gender):
        self.gender = gender

    def getage(self):
        return self.age
    
    def setage(self,age):
        self.age = age

    def getsalary(self):
        return self.salary
    
    def setsalary(self,salary):
        self.salary = salary

    def get_gratuaty(self):
        grat = Employee.calculategratuaty(self.years, Employee.yearamount, Employee.gratuaty_percent)
        return grat

    @staticmethod
    def calculategratuaty(years, yearamount, percent):
        return years * yearamount * percent


if __name__ == "__main__":
    # # print(__name__)
    # # print(e1)
    # # print(type(e1))
    # emp1 = Employee("Vinayak","M",39,26000000)
    # print(emp1.__dict__)
    # emp1.setname("Vinayak Sadanand Subhedar")
    # emp1.setgender("Male")
    # emp1.setage(40)
    # emp1.setsalary(4000000)
    # print(emp1.__dict__)
    # print(type(emp1))

    # #Built in Functions
    # #getattr,setattr,delattr,hasattr
    # emp1_age = getattr(emp1,"age")
    # print(emp1_age)
    # setattr(emp1,"age",30)
    # print(emp1.age)
    # checkattrage = hasattr(emp1,"age")
    # print(checkattrage)
    # delattr(emp1,"age")
    # checkattrage = hasattr(emp1,"age")
    # print(checkattrage)

    # #Built in class attributes

    # print(Employee.__dict__)
    # print(Employee.__doc__)
    # print(Employee.__name__)
    # print(Employee.__module__)
    # print(Employee.__bases__)

    # #isinstance
    # emp2 = None
    # #chkisinstance = isinstance(emp1,Employee)
    # print(isinstance(emp2,Employee))
    # emp1 = Employee("Vinayak","M",39,26000000)
    # emp1 = Employee("Disha","M",39,26000000)
    # emp1 = Employee("Pankti","M",39,26000000)
    # emp1 = Employee("Aarya","M",39,26000000)
    # emp1 = Employee("Reyaansh","M",39,26000000)
    # print(Employee.getnoofstudents())
    # print(Employee.no_of_students)
    emp1 = Employee("Vinayak","M",39,26000000)
    print(emp1.get_gratuaty())