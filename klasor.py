import os
filename = "04_01_Egzersiz1"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"

def toplam(a,b):
    print(a+b)
toplam(3,4)

yukarıdaki kod bloğundan faydalanarak 4 işlem için birbirinden farklı 4
fonksiyon yazınız
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
