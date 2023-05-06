
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm çift sayıların toplamını return deyimi ile dönen fonksiyonu 
yazınız. 
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""
def sayilar(*args):
    liste=[2,4,6,8,10]
    sonuc=0
    for item in liste:
        if item%2==0:
            sonuc=sonuc+item
    return sonuc
print(sayilar())


   


 


    
  

