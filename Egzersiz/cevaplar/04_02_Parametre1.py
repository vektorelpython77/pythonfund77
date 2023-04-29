
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

def bilgi(adi,soyadi,eposta=""):
    print(f"""
    ########################
    Adı : {adi}
    Soyadı : {soyadi}
    E-Posta : {eposta if eposta else "E Posta Yok"} 
    ########################
    """)

    #   if eposta:
    #     print(eposta)
    #   else:
    #     print("E Posta Yok")
    ###########################
    ##  eposta if eposta else "E Posta Yok"

bilgi("İbrahim","EDİZ","edizdesign@gmail.com")
bilgi("İbrahim","EDİZ",)