import copy

class Prototype:
    def clone(self):
        pass

class Car(Prototype):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"{self.year}:{self.make}:{self.model}"
    


if __name__ == "__main__":
    """
    This is predefined template in the system
    Guess We are using survey template which is already exist rather than creating new template.
    This will allow us to change only required setting areas.

    If we are designing template from scratch, it will not be used.
    """
    car_2024 = Car("Toyota","Corolla",2024)

    car_2025 = car_2024.clone()


    print(car_2024==car_2025)
    car_2025.year = 2025

    print(car_2024)
    print(car_2025)

    
