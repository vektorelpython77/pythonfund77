
"""
Elimizde kare,diktörgen ve ücgen levhalar var
Bu levhaları üzerinde işlemler gerçekleştiriyoruz.
Bizim için bu levhaların üçünün de ortak özelliklerini ve fonksiyonlarını bir arada
tutabilecek bir sınıf oluşturmanı istiyoruz. Sınıfın isminin Cokgen olmasını bekliyoruz
özellikler ve metotlar sana kalmış...
başarılar
"""

class Cokgen:
    tur = "Çokgen Levhalar" # class attribute
    def __init__(self,adi,hammadde,kalinlik): 
        self.adi = adi # initialize - constructor(Yapıcı)
        self.hammade = hammadde# instance attribute
        self.kalinlik= kalinlik
       
    @classmethod
    def turSoyle(cls): # class method
        print(cls.tur)

    def __del__(self):
        print("RIP",self.adi)


Ucgen = Cokgen("Üçgen Levha") # instance Object Nesne
Kare = Cokgen ("Kare levha") # instance Object Nesne
Dortgen=Cokgen("5 Gen levha")
print("Ucgen için fonksiyon çalışıyor")
Ucgen.adiSoyle()
print("Kare için fonksiyon çalışıyor")
Dortgen.adiSoyle()
print("Dortgen için fonksiyon çalışıyor")
Kare.adiSoyle()
Ucgen.turSoyle()
Kare.turSoyle()

Cokgen.turSoyle()