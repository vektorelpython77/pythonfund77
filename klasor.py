import os
filename = "02_01_giris"
liste = os.listdir("Egzersiz/")
for item in liste:
    open(f"Egzersiz/{item}/{filename}.py","a+")
# TODO veri tabanı bağlantrısı eklenecek 
