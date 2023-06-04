from abc import ABC,abstractmethod

class Urun(ABC): 
    @abstractmethod
    def urunIdGetir(self):
        pass

# obj1 = Urun() # Can't instantiate abstract class Urun with abstract method urunIdGetir
class Rulman(Urun):
    def __init__(self):
        self.urunId = "RLM2023251452"
    
    def urunIdGetir(self):
        return self.urunId
    
obj1 = Rulman()
print(obj1.urunIdGetir())