"""
class ==> Sınıf
instance ==> Örnek

attribute ==> Özellik
method ==> metot
"""

class Ucak:
    tur = "Savaş Uçakları" # class attribute
    def __init__(self,adi,ulke,fiyat): 
        self.adi = adi # initialize - constructor(Yapıcı)
        self.ulke = ulke# instance attribute
        self.fiyat= fiyat
       
    @classmethod
    def turSoyle(cls): # class method
        print(cls.tur)

    def __del__(self):
        print("RIP",self.adi)


Ucak1 = Ucak("F-16") # instance Object Nesne
Ucak2 = Ucak("Su-35") # instance Object Nesne
print("Ucak1 için fonksiyon çalışıyor")
Ucak1.adiSoyle()
print("Ucak2 için fonksiyon çalışıyor")
Ucak2.adiSoyle()
Ucak1.turSoyle()
Ucak2.turSoyle()
Ucak.turSoyle()

 
