"""
1. tell
2. seek
3. truncate
4. close
"""
adres = "Projeler\Dosyalamaİslemleri\ornek.csv"
kip="r+"
dosya = open(adres,kip,encoding="UTF-8")
dosya.read()
print(dosya.tell())
dosya.seek(20)
print(dosya.tell())
################## örnek
dosya.seek(0)
dosya.read()
dosya.seek(0)
############# truncate
dosya.seek(0)
print(dosya.read())
dosya.seek(25)
dosya.truncate()
dosya.seek(0)
print(dosya.read())


# adres = "Projeler\Dosyalamaİslemleri\ornek2.csv"
# kip="a+"
# dosya = open(adres,kip,encoding="UTF-8")
# adi = input("Adını Giriniz:")
# soyadi = input("Soyadını Giriniz:")
# telefon = input("Telefon Giriniz")
# metin = ";".join([adi,soyadi,telefon])
# print(metin,file=dosya)
# input()

# adres = "Projeler\Dosyalamaİslemleri\ornek2.csv"
# kip="a+"
# dosya = open(adres,kip,encoding="UTF-8")

# with  open(adres,kip,encoding="UTF-8") as dosya:
#     adi = input("Adını Giriniz:")
#     soyadi = input("Soyadını Giriniz:")
#     telefon = input("Telefon Giriniz")
#     metin = ";".join([adi,soyadi,telefon])
#     print(metin,file=dosya)
# input()




adres = "Projeler\Dosyalamaİslemleri\ornek2.csv"
kip="a+"
dosya = open(adres,kip,encoding="UTF-8")
adi = input("Adını Giriniz:")
soyadi = input("Soyadını Giriniz:")
telefon = input("Telefon Giriniz")
metin = ";".join([adi,soyadi,telefon])
print(metin,file=dosya)
dosya.close()
input()