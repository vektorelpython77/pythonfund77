import os
filename = "04_02_Parametre1"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"

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
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
