
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm çift sayıların toplamını return deyimi ile dönen fonksiyonu 
yazınız. 
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız

"""
def fonk(liste):
    result=1
    for item in liste:
        result*=item
    return result
print(fonk([1,2,3,3,3]))