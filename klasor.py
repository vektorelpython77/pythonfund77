import os
filename = "04_04_Egzersiz2"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
istenilen uzunlukta ve aşağıdaki kriterleri sağlayan şifre üreten
fonksiyonu yazınız
1. en az bir küçük harf olmalıdır
2. en az bir büyük harf olmalıdır
3. en az bir rakam olmalıdır
4. en az bir noktalama işareti olmalıdır

from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import random as rnd

yukarıdaki kütüphanelerden faydalanabilirsiniz.
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
