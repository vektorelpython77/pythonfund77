import os
filename = "02_06_set"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
import random as rnd
rnd.seed(0)
liste1 = [rnd.randint(1,50) for i in range(20)]
liste2 = [rnd.randint(1,50) for i in range(20)]
##################################################
yukarıdaki listelerden faydalanarak 
iki liste arasındaki farkı ve ortak sayıları bulan 
python kodunu yazınız

\"\"\"
"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı eklenecek 


# https://codeshare.io/eVn8ml
