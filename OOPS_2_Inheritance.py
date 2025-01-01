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



class Customer(Person):
    def __init__(self,cust_id,dor,gender,dob,address,city,district,state, country):
        super().__init__(gender,dob,address,city,district,state, country)
        self.custid = cust_id
        self.dor = datetime.strptime(dor, "%Y-%m-%d")

    def getrelationyears(self):
        return super().getdatediff(self.dor)

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

class Country:
    capital = "Delhi"
    def __init__(self):
        self.type = "Country Wala"
    #capital = None
    #pass

class State:
    capital = "Mumbai"
    def __init__(self):
        #self.tt = "Vinayak"
        self.role = None
    #pass

class City(State,Country):
    capital = "Lower Parel"
    def __init__(self):
        super().__init__()
        #self.type = "City Wala"
    #pass

if __name__ =="__main__":
    print("Person Class Data")
    vinayak = Person("Male","1984-08-21","G-403, IRIS, Rajhanse Kshitij","Vasai","Palghar","Maharashtra", "India")
    print(vinayak.__dict__) 
    print(vinayak.getage())
    print("########## Inheritance of Person class with Employee class")
    vinayak = Employee(163460,"2022-11-14","Male","1984-08-21","G-403, IRIS, Rajhanse Kshitij","Vasai","Palghar","Maharashtra", "India")
    print(vinayak.__dict__) 
    print(vinayak.getexperinece())
    print(vinayak.getage())
    print("########## Inheritance of Person class with Customer class")
    vinayak = Customer(163460,"2022-11-14","Male","1984-08-21","G-403, IRIS, Rajhanse Kshitij","Vasai","Palghar","Maharashtra", "India")
    print(vinayak.__dict__) 
    # getexperinece() is from Employee class which is abother child class of Person. It will not work with another child class Customer
    #print(vinayak.getexperinece())
    print(vinayak.getrelationyears())
    print(vinayak.getage())

    #Multiple Inheritance
    print("#Multiple Inheritance")
    mumbaikar = City()
    print(mumbaikar.capital)
    print(mumbaikar.type)