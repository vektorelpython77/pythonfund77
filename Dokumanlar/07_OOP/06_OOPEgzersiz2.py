class A:
    def __init__(self):
        self.__gizli = "SECRET"
    
    @property
    def gizli(self): # getter
        return self.__gizli

    @gizli.setter
    def gizli(self,param):
        if type(param) == int:
            self.__gizli = param
        else:
            raise Exception("Değer Hatası")
        
    @gizli.deleter
    def gizli(self):
        self.__gizli *= -1
    
obj1 = A()
print("İlk Değer=>",obj1.gizli)
obj1.gizli = 2
print("Değiştirdikten sonra=>",obj1.gizli)
del obj1.gizli
print("Sildikten Sonra => ",obj1.gizli) 
    

    

        