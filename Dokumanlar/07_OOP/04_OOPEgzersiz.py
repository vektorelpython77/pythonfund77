import time
import random

class Hero:
    def __init__(self,adi,guc,saglik):
        self.adi = adi
        self.guc = guc
        self.saglik = saglik
        self.adim = 0
    def vurma(self):
        fonk = [self.vurma1,self.vurma2,self.vurma3]
        return random.choice(fonk)()

    def vurma1(self):
        return self.guc//2

    def vurma2(self):
        return self.guc//3

    def vurma3(self):
        return self.guc

    def darbe(self,Pguc):
        fonk = [self.darbe1,self.darbe2,self.darbe3]
        random.choice(fonk)(Pguc)

    def darbe1(self,Pguc):
        self.saglik -= Pguc//2
        
    def darbe2(self,Pguc):
        self.saglik -= Pguc//3

    def darbe3(self,Pguc):
        self.saglik -= Pguc

    def bilgi(self):
        print(self.adi,"=>",self.saglik)


class MarvelHero(Hero):
    tur = "MarvelHero"
    def __init__(self,adi,guc,saglik):
        super().__init__(adi,guc,saglik)
        self.superGuc = saglik

    def vurma(self):
        self.adim += 1
        return super().vurma()

    def darbe(self,Pguc):
        if self.adim > random.randint(1,10):
            print(self.adi,"Super Güç Kullandı")
            self.adim = 0
            self.saglik = self.superGuc
        super().darbe(Pguc)


class DCHero(Hero):
    tur = "DC Hero"
    def __init__(self,adi,guc,saglik):
        super().__init__(adi,guc,saglik)
        self.superGuc = guc

    def darbe(self,Pguc):
        self.adim += 1
        super().darbe(Pguc)

    def vurma(self):
        if self.adim > random.randint(1,10):
            self.adim = 0
            print(self.adi,"Super Güç Kullandı")
            return self.superGuc*2
        else:
            return super().vurma()

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool",100,1500)


class Hulk(MarvelHero):
    def __init__(self):
        super().__init__("Hulk",110,1400)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("CaptainAmerica",95,1700)

class Batman(DCHero):
    def __init__(self):
        super().__init__("Batman",100,1500)

class Flash(DCHero):
    def __init__(self):
        super().__init__("Flash",105,1450)

class SuperMan(DCHero):
    def __init__(self):
        super().__init__("SuperMan",95,1650)



Mliste = [DeadPool,Hulk,CaptainAmerica]
DListe = [Batman,Flash,SuperMan]




P1 = random.choice(Mliste)()
P2 = random.choice(DListe)()
print("P1 için ",P1.adi,"Seçildi")
print("P2 için ",P2.adi,"Seçildi")
while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(0.5)
    P2.darbe(P1.vurma())
    P1.darbe(P2.vurma())
    P1.bilgi()
    P2.bilgi()
else:
    if P1.saglik>P2.saglik:
        print(P1.adi,"Kazandi")
    elif P1.saglik<P2.saglik:
        print(P2.adi,"Kazandi")
    else:
        print("Berabere")
    print("Oyun Bitti")