from datetime import datetime
class Person:
    def __init__(self,gender,dob,address,city,district,state, country):
        self.gender= gender
        self.dob = datetime.strptime(dob, "%Y-%m-%d")
        self.address = address
        self.city = city
        self.district = district
        self.state = state
        self.country = country

    @staticmethod
    def getdatediff(date):
        today = datetime.today()
        datediff = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
        return datediff


    def getage(self):
        return Person.getdatediff(self.dob)
        # today = datetime.today()
        # age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        # return age



class Customer:
    pass

class Employee(Person):
    def __init__(self,id,doj,gender,dob,address,city,district,state, country):
        super().__init__(gender,dob,address,city,district,state, country)
        self.id = id
        self.doj = datetime.strptime(doj, "%Y-%m-%d")

    def getexperinece(self):
        return super().getdatediff(self.doj)
        # today = datetime.today()
        # experience = today.year - self.doj.year - ((today.month, today.day) < (self.doj.month, self.doj.day))
        # return experience





if __name__ =="__main__":
    # vinayak = Person("Male","1984-08-21","G-403, IRIS, Rajhanse Kshitij","Vasai","Palghar","Maharashtra", "India")
    # print(vinayak.__dict__) 
    # print(vinayak.getage())
    vinayak = Employee(163460,"2022-11-14","Male","1984-08-21","G-403, IRIS, Rajhanse Kshitij","Vasai","Palghar","Maharashtra", "India")
    print(vinayak.__dict__) 
    print(vinayak.getexperinece())
    print(vinayak.getage())