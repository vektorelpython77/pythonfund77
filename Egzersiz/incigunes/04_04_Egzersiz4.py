
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm sayıların çarpımını hesaplayan fonksiyonu yazınız
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""

def carpim(liste):
    
    result = 1
    for item in liste:
        result *= item
    return result

liste = [1, 2, 3, 4, 5] 
print(carpim(liste)) 
