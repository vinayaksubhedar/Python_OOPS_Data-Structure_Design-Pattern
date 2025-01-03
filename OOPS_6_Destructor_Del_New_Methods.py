class Employee:
    _instance = None
    def __new__(cls,*args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,name,age,gender):
        if not hasattr(self, '_initialized'):
            self.name = name
            self.age = age
            self.gender = gender
            self._initialized = True

    # def __new__(cls, *args):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    # def __init__(self, name, age, gender):
    #     if not hasattr(self, '_initialized'):  # Initialize only once
    #         self.name = name
    #         self.age = age
    #         self.gender = gender
    #         self._initialized = True  # Set the flag

    def __del__(self):
        print("Distructor called")

e1 = Employee("Vinayak",40,"male")
e2 = Employee("Pravin",42,"male")


print(f"Age of {e1.name} is {e1.age}. Gender is {e1.gender}")
print(f"Age of {e2.name} is {e2.age}. Gender is {e2.gender}")

