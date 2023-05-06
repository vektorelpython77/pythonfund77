
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm sayıların çarpımını hesaplayan fonksiyonu yazınız
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""
x=[1,2,3,4,5,6,7,8,9,10]

def carp(*args):
    
    t=1
    for item in x:
        t*=item
    return t
print(carp())