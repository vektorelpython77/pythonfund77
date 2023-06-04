
"""
Bir şarküteri  ürettiği ürünleri yapay zeka ile 
ilişkilendirerek bir proje yapmak istemektedir.
Bu işlem için bazı kurallar belirlenmesi gerekmiştir. İlk kuralın 
her ürüne çeşidine ait bir URUNID numarası olduğu bilinmektedir. 
Yazılımcı olarak bu numaranın tüm sınıflarda olmasını sağlayacak 
durumu yazınız.

"""

from abc import ABC,abstractmethod
class Urun(ABC):
    @abstractmethod
    def urunIdGetir(self):
        pass

class Salam(Urun):
    def __init__(self):
        self.urunId = "SALAM012023"


    def urunIdGetir(self):
        return self.urunId

urun1 = Salam()
print(urun1.urunIdGetir()) 