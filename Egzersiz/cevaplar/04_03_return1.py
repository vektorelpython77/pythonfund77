
"""

Faktoriyel hesabı yapan bir fonksiyon yazalım 
fonksiyon sonucu dışarı return deyimi ile göndersin.
print fonksiyonu ve yazdığımız faktoriyel fonksiyonunu 
birlikte kullanıp sonucu
ekrana yazdıralım.
"""

def faktoriyel(sayi):
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))

def faktoriyel2(sayi):
    import math
    return math.factorial(sayi)


print(faktoriyel2(5))

def faktoriyel3(sayi):
    if sayi == 1:
        return 1
    else:
        return faktoriyel3(sayi-1) * sayi

print(faktoriyel3(5))