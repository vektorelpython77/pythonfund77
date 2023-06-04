class Ediz:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls) 
        return inst
    def __init__(self):
        print("init çalıştı")
        self.param = "param"


    def __le__(self,obj): # less than equal
        return self.param >= obj.param
    


    def __iadd__(self,obj):
        self.param += obj.param
        return self.param
    
    def __eq__(self,obj):
        return obj.param == self.param

    # def __del__(self):
    #     print("Silindi")
    #     self.param = 0        

    def __str__(self):
        return str(self.param)


sayi1 = Ediz()
sayi2 = Ediz()
print(sayi1 <= sayi2) 
print(sayi1 == sayi2)
sayi2 += sayi1
print(sayi1)
print(sayi2) 

