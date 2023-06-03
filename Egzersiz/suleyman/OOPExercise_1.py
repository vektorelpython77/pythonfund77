
"""

"""

class Araba:
    tur = "Otomobil"
    def __init__(self,marka,model): 
        self.marka = marka 
        self.model = model
    
    def bilgi(self): 
        print(self.model)


    @classmethod
    def bilgi1(cls):
        print(cls.tur)

    def __del__(self):
        print("RIP",self.model)


araba1 = Araba("Ford","Mondeo") 
araba2 = Araba("Audi","A6") 
araba1.bilgi()
araba2.bilgi()
araba1.bilgi1()
araba2.bilgi1()
