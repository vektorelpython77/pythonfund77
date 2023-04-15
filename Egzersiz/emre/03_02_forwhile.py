
"""
sayısal loto oyununda 1,49 sayıları arasındaki sayılardan 
6 adet sayının seçilmesi gerekmektedir.
1. Alternatif 
from random import randint
randint(1,49)
2. Alternatif
from random import choice
liste = [i for i in range(1,50)]

yukarıdaki kod bloklarında faydalanarak 
istenilen sayıda sayısal loto kolonu oynayan python kodunu 
yazınız
ipucu while ve for döngüleri birlikte kullanılmaktadır. 
"""

from random import randint
buyukListe = []
for j in range(int(input("Kolon Sayısını Giriniz:"))):
    liste = []
    for i in range(1,7):
        sayi = randint(1,49)
        while sayi in liste:
            sayi = randint(1,49)
        liste.append(sayi)
    else:
        liste.sort()
        buyukListe.append(liste)
else:
    print(*buyukListe,sep="\n")