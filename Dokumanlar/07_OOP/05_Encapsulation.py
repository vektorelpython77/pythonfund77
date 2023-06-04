
"""
__gizli => gizli değişken
__gizli_ => gizli değişken
__gizli__ => GİZLİ DEĞİŞKEN DEĞİL
"""

class A:
    def __init__(self,yetki):
        self.yetki = yetki
        self.__gizli = "SECRET"

    @property
    def gizli(self): #getter
        if self.yetki == 1:
            return self.__gizli
        else:
            raise Exception("Yetki Hatası")
        
    @gizli.setter
    def gizli(self,param):
        if self.yetki == 1:
            if type(param) == int and param in range(20,30):
                self.__gizli = param
            else:
                raise Exception("Değer Hatası")
        else:
            raise Exception("Yetki Hatası")
        
    @gizli.deleter
    def gizli(self):
        self.__gizli *= -1

    def method(self):
        return self.a
    

try: 
    obj1 = A(1)
    obj2 = A(2)
    print(obj1.gizli)
    obj1.gizli = 25
    print(obj1.gizli)
    del obj1.gizli
    print(obj1.gizli)
except Exception as hata:
    print(hata)


