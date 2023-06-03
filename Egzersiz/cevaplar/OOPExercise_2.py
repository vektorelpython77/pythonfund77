
"""
Elimizde kare,diktörgen ve ücgen levhalar var
Bu levhaları üzerinde işlemler gerçekleştiriyoruz.
Bizim için bu levhaların üçünün de ortak özelliklerini ve fonksiyonlarını bir arada
tutabilecek bir sınıf oluşturmanı istiyoruz. Sınıfın isminin Cokgen olmasını bekliyoruz
özellikler ve metotlar sana kalmış...
başarılar
"""


class Cokgen:
    def __init__(self,adi,malzeme,kenarolcu,aci):
        self.adi = adi
        self.malzeme = malzeme
        self.kenarolcu = kenarolcu
        self.aci = aci

    def aciSoyle(self):
        return self.aci

    def bilgiVer(self):
        return [self.adi,self.malzeme,self.kenarolcu,self.aci]

    def adiSoyle(self):
        return self.adi

ucgen = Cokgen("Üçgen","Ahşap",[12,10,12],[45,90,45])
kare = Cokgen("Kare","Demir",[10,10,10,10],[90,90,90,90])
dikdortgen = Cokgen("Dikdörtgen","Çelik",[20,50,20,50],[90,90,90,90])
print(ucgen.aciSoyle())
print(kare.aciSoyle()) 
    
a = 5
print(type(a))   #<class 'int'>
print(type(ucgen)) # <class '__main__.Cokgen'>
