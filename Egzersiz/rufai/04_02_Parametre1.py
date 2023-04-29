"""

def topla(a,b,c=0):
    print(a+b+c)

yukarıda yer alan örnekten faydalanarak 
adi,soyadi ve email adresini parametre olarak alıp;

########################
Adı : Örnek
Soyadı : Örnek
E-Posta : ornek@ornek.com
########################
şeklinde ekrana yazdıran fonksiyonu yazınız.
e posta adresi girilmesi gerekmediği durumda kullanıcı 
fonk("Ornek","Ornek") şeklinde fonksiyonu çalıştırabilsin.
"""
def tanim(ad,soyad,email=""):
    print(f"{ad} {soyad} {email}")
tanim("Ali","Veli","ab@gmail.com")


