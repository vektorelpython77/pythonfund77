
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm çift sayıların toplamını return deyimi ile dönen fonksiyonu 
yazınız. 
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""

def toplam_cift_sayilar(liste):
    ciftlerin_toplami = 0
    for sayi in liste:
        if sayi % 2 == 0:
            ciftlerin_toplami += sayi
    return ciftlerin_toplami
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(toplam_cift_sayilar(liste))


    