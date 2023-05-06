
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm sayıların çarpımını hesaplayan fonksiyonu yazınız
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""

def fonk(liste):
    result=0
    for item in liste:
        result*=item
    return result
print(fonk({1,2,3,4,55,4,7,35}))