class Ferrari:
    def __init__(self,model,fuel_type,max_speed):
        self.model = model
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def get_fuel_type(self):
        return self.fuel_type
    
    def get_max_speed(self):
        return self.max_speed
    
class BMW:
    def __init__(self,model,fuel_type,max_speed):
        self.model = model
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def get_fuel_type(self):
        return self.fuel_type
    
    def get_max_speed(self):
        return self.max_speed
    
def car_details(obj):
    print(obj.get_fuel_type())
    print(obj.get_max_speed())


if __name__ == "__main__":
     ferrari = Ferrari("F1","Diesel",500)
     print("____ Ferarri _____")
     car_details(ferrari)
     bmw = BMW("S1","Petrol",300)
     print("____ BMW _____")
     car_details(bmw)