class Decorator:
    def __init__(self,func):
        self.func = func
    
    def __call__(self,basic,da,hra):
        result = self.func(basic,da,hra) - (basic * 0.10)
        return result
    

#d1 = Decorator()

@Decorator
def sal(basic,da,hra):
    return basic + da + hra


#print(d1(10,30))

print(sal(40000,10000,15000))


def decofunction(fun):
    def wrapper(basic,da,hra):
        return fun(basic,da,hra) - (basic * 0.10)
    return wrapper

@decofunction
def sal1(basic,da,hra):
    return basic + da + hra

print(sal1(40000,10000,15000))