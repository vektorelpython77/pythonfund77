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
dosya = open("Projeler\Dosyalamaİslemleri\ornek.txt",encoding="UTF-8")
# hiç bir bilgi yazmazsak okuma modunda açar
print(dosya.read())
