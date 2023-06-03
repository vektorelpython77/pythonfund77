class A: # parent
    def __init__(self):
        self.a = "A"

    def soyleA(self):
        print(self.a)

    def soyle(self):
        print("A Sınıfından Çalıştım")


class B(A):
    def __init__(self): # overload
        super().__init__() 
        self.b = "B"
    
    def soyleB(self):
        print(self.b)


    def soyle(self): # override
        print("----B Sınıfın Çalıştım")


def fonk(obj):
    obj.soyle()

obj1 = A()
obj2 = B()
liste = [obj1,obj2]
for item in liste:
    fonk(item) 