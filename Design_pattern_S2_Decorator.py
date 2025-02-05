class Coffee:
    def cost(self):
        return 5
    

class MilkDecorator:
    def __init__(self, Coffee):
        self.Cofee = Coffee
    def cost(self):
        return self.Cofee.cost() + 2


if __name__ == "__main__":
    mycoffee = Coffee()

    mymilkcoffee = MilkDecorator(mycoffee)

    print(mymilkcoffee.cost())
