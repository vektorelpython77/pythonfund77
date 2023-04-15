
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
maks = 100
mini = 0
adim = 0
while True:
    tahmin = mini + (maks-mini)//2
    giris = input(f"Sayı : {tahmin} A:1,Y:2,D:3 ======:")
    adim += 1
    if giris == "1":
        maks = tahmin
    elif giris == "2":
        mini = tahmin
    elif giris == "3":
        print(f"Sayı = {tahmin} {adim} kadar adımda buldum")
        break
