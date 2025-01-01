"""
Operator Overloading
10 + 20 = 30
"10" + "20" = "1020"
"""
#print(dir(int))

"""Operator Overload"""
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self,other):
        return Book("New Additional",self.pages + other.pages)
    def __str__(self):
        return str(self.pages)
    
"""Method Overload"""
class Calci:
    def add(self,*args):
        addition = 0
        for arg in args:
            addition = addition + arg
        return addition


if __name__ == "__main__":
    # b1 = Book("Vinayak", 1000)
    # b2 = Book("Disha",2000)
    # b3 = Book("Reyaansh",4000)
    # print(b1 + b2 + b3)

    c1 = Calci()

    print(c1.add(10,20,30))