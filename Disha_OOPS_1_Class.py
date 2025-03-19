# How to Create a class in Python
##### ---- Lecture 1 ---- #####
# class Person:
#     pass



# if __name__ == "__main__":
# p1 = Person()
# print(p1)
'''
<__main__.Person object at 0x000001CA949D3460>

__main__ : 
-- This refers to the module (or script) where the class Person is defined.
-- If you run a script directly in Python, it gets the name "__main__". 
   So, __main__.Person means the class Person is defined in the main script.

Person :
--  This is the name of the class from which the object is created.
--  This means that an instance of the Person class has been created.

0x000001CA949D3460 : 
-- This indicates the memory address where the object is stored.
-- 0x000001CA949D3460 is a hexadecimal representation of the memory location.
'''

##### ---- Lecture 2 ---- Constructor - Passing Values #####
# from datetime import datetime
# class Person:
#     def __init__(self,firstname:str,middlename:str,lastname:str,date_of_birth:datetime):
#         self.firstname = firstname
#         self.middlename = middlename
#         self.lastname = lastname
#         self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")


# if __name__ == "__main__":
#     P001 = Person("Sachin","Ramesh","Tendulkar","1973-04-24")
#     print(P001.__dict__)
    # print(P001)
    # print(P001.firstname)
    # print(P001.middlename)
    # print(P001.lastname)
    # print(P001.date_of_birth)

    # P001.firstname = "Virat"
    # P001.middlename = "Prem"
    # P001.lastname = "Kohli"
    # P001.date_of_birth = "1988-11-05"

    # print(P001)
    # print(P001.firstname)
    # print(P001.middlename)
    # print(P001.lastname)
    # print(P001.date_of_birth)



##### ---- Lecture 3 ---- Encapsulation #####
from datetime import datetime
class Person:
    def __init__(self,firstname:str,middlename:str,lastname:str,date_of_birth:datetime):
        self.__firstname = firstname
        self.__middlename = middlename
        self.__lastname = lastname
        self.__date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")


if __name__ == "__main__":
    P001 = Person("Sachin","Ramesh","Tendulkar","1973-04-24")
    print(P001.__dict__)
    print(P001._Person__firstname)
    P001._Person__firstname = "Sachu"
    print(P001.__dict__)
    print(P001._Person__firstname)
    # print(P001)
    # print(P001.firstname)
    # print(P001.middlename)
    # print(P001.lastname)
    # print(P001.date_of_birth)

    # P001.firstname = "Virat"
    # P001.middlename = "Prem"
    # P001.lastname = "Kohli"
    # P001.date_of_birth = "1988-11-05"

    # print(P001)
    # print(P001.firstname)
    # print(P001.middlename)
    # print(P001.lastname)
    # print(P001.date_of_birth)

##### ---- Lecture 4 ---- Getter and Getter Method#####
# from datetime import datetime
# class Person:
#     def __init__(self,firstname:str,middlename:str,lastname:str,date_of_birth:datetime):
#         self.firstname = firstname
#         self.middlename = middlename
#         self.lastname = lastname
#         self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

#     def getFullName(self):
#         return f"{self.firstname} {self.middlename} {self.lastname}".strip() 
    

#     def getAge(self):
#         today = datetime.today()
#         age = today.year - self.date_of_birth.year
#         if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# if __name__ == "__main__":
#     P001 = Person("Rohit","Kumar","Sharma","1990-05-15")
#     print(P001.getAge())
#     print(P001.getFullName())