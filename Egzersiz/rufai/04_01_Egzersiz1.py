
"""

def toplam(a,b):
    print(a+b)
toplam(3,4)

yukarıdaki kod bloğundan faydalanarak 4 işlem için birbirinden farklı 4
fonksiyon yazınız
"""
def toplam(a,b):
    print(a+b)
toplam(1,2)

def cikarma(a,b):
    print(a-b)
cikarma(8,6)

def bolme(a,b):
    print(a/b)
bolme(10,20)

def carpma(a,b):
    print(a*b)
carpma(9,8)


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