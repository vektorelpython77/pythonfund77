
"""
Elimizde kare,diktörgen ve ücgen levhalar var
Bu levhaları üzerinde işlemler gerçekleştiriyoruz.
Bizim için bu levhaların üçünün de ortak özelliklerini ve fonksiyonlarını bir arada
tutabilecek bir sınıf oluşturmanı istiyoruz. Sınıfın isminin Cokgen olmasını bekliyoruz
özellikler ve metotlar sana kalmış...
başarılar
"""

class Cokgen:
    def __init__(self,kenar_sayısı,acı):
        self.kenar_sayısı=kenar_sayısı
        self.acı=acı

    def sorgu(self):
        print(self.kenar_sayısı)
        print(self.acı)



kare=Cokgen("4","90 derece")
eşkenar_ucgen=Cokgen("3","60 derece")

kare.sorgu()
eşkenar_ucgen.sorgu()
