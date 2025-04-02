class Smartphone:
    def __init__(self, brand, storage):
        self.brand = brand
        self.storage = storage  
    def fun(self):
        print(f"its greate {self.brand} have storage {self.storage} GB")
class Phone(Smartphone):
    pass
phone1 = Smartphone("Sumsung A52", 128)
phone1.fun()
phone2 = Phone("IPhone A14",  256 )
phone2.fun()
