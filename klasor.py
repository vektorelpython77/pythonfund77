import os
filename = "01_02_input"
liste = os.listdir("Egzersiz/")
for item in liste:
    open(f"Egzersiz/{item}/{filename}.py","a+")
# TODO veri tabanı bağlantrısı eklenecek 
