class Salary:
    def __init__(self, basic):
        self.basic = basic

    @property
    def hra(self):
        return self.basic * 0.10

    @hra.setter
    def hra(self,value):
        self.basic = value * 0.10

    @hra.deleter
    def hra(self):
        self.basic = None

    
if __name__ == "__main__":
    s1 = Salary(57000)
    #print(s1.hra())
    print(s1.hra)
    s1.hra = 600000
    print(s1.hra)

    del s1.hra
    print(s1.basic)
