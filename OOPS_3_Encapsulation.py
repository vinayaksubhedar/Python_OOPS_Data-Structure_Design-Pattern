"""
1. Encapsulation
2. Access Modifier
3. Name mangling
4. Private methods
# To convert any variable as a private or any method as a private prefix it with "__"
"""

class Finance:
    def __init__(self):
        self.__revenue = 1000000

    def getrevenue(self):
        return self.__revenue
    
    def setrevenue(self,revenue):
        self.__revenue = revenue

f1 = Finance()
#print(f1.revenue) # Encapsulation
print(f1.getrevenue())
f1.setrevenue(2000000)
print(f1.getrevenue())
#hack
print(f1.__dict__) #name Mangling
print(f1._Finance__revenue)
f1._Finance__revenue = 3000000
print(f1._Finance__revenue)


