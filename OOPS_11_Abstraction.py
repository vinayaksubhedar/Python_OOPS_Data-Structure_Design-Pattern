"""
1. Abstract class is blank blueprint - Signatures
2. All abstracts methods should be defined in child classes otherwise it gives error
3. Abstract class should have atleast one abstract method
4. Abstract class can not be instantiated(Can not create object)
"""


from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def milage(self):
        pass

    @abstractmethod
    def airbags(self):
        pass

    def color(self):
        print("white")

class MarutiSuzuki(Car):
    def milage(self):
        print("This is Maruti Milage")

    def airbags(self):
        print("Maruti Suzuki has 4 wipers")

class Tata(Car):
    def milage(self):
        print("This is Tata Milage")

    def airbags(self):
        print("Tata has 6 wipers")


car1 = MarutiSuzuki()
car2 = Tata()

car1.milage()
car2.milage()

car1.airbags()
car2.airbags()