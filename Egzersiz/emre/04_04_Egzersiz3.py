
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm çift sayıların toplamını return deyimi ile dönen fonksiyonu 
yazınız. 
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""
x=[1,2,3,4,5,6,7,8,9,10]
def cift(x):
    for num in x:
        if num %2==0:
            print(num)

print(cift(x))
