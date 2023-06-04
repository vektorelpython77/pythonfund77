"""
class ==> Sınıf
instance ==> Örnek

attribute ==> Özellik
method ==> metot
"""

class Kedi:
    tur = "Ev Kedisi" # class attribute
    def __init__(self,adi):  # initialize - constructor(Yapıcı)
        self.adi = adi # instance attribute
        self.beslendi = False # instance attribute
    
    def adiSoyle(self): # instance method
        print(self.adi)
    
    def beslenme(self):
        print(self.adi,"beslendi")
        self.beslendi = True

    def beslendimi(self):
        print(self.adi,self.beslendi)
    

    @classmethod
    def turSoyle(cls): # class method
        print(cls.tur)

    def __del__(self):
        print("RIP",self.adi)


kedi1 = Kedi("Misket") # instance Object Nesne
kedi2 = Kedi("Boncuk") # instance Object Nesne
kedi1.beslenme()
kedi1.beslendimi()
kedi2.beslendimi()

# https://codeshare.io/78zzko


"""
02_Inheritance ==> Kalıtım
03_Polymorphism ==> Çok Biçimlilik
05_Encapsulation ==> Kapsülleme
06_Abstraction ==> Soyutlama
"""