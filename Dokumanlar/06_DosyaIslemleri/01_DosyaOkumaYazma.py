"""
Dosya türleri
metin tabanlı dosyalar örn: txt,csv
binary dosyalar örn: jpg,pdf
"""
"""
yol
1. Full Path  
### D:\İbrahimEDİZ\python77\Projeler\Dosyalamaİslemleri\ornek.txt
2. Relative Path
### Projeler\Dosyalamaİslemleri\ornek.txt
"""
"""
Dosya açma modları
r read => Okuma 
w write => Yazma
a append => Sona Ekleme Yazma
x create => Oluşturma Yazma
r+ Hem okuma Hem Yazma
w+ Hem okuma Hem Yazma
a+ Hem okuma Hem Yazma
x+ Hem okuma Hem Yazma
###############################
binary dosya için 
rb,rb+
wb,wb+
ab,ab+
xb,xb+
"""

"""
Denemeler
"""
################# 1.
adres = "Projeler\Dosyalamaİslemleri\ornek.csv"
kip="r+"
dosya = open(adres,kip,encoding="UTF-8")
bilgi = "Ali;Veli;123\n"
# for i in range(8):
#     dosya.write(bilgi)
print("1",dosya.read())
# print("2",dosya.read())