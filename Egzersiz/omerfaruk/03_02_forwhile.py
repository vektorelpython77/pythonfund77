
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
sayi = 128452


birlerbsm    = sayi%10
onlarbsm     = (sayi%100)//10
yüzlerbsm    = (sayi%1000)//100
binlerbsm    = (sayi%10000)//1000
onbinlerbsm  = (sayi%100000)//10000
yüzbinlerbsm = (sayi%1000000)//100000

print(birlerbsm)
print(onlarbsm)
print(yüzlerbsm)
print(binlerbsm)
print(onbinlerbsm)
print(yüzbinlerbsm)