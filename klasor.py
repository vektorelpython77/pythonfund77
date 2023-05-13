import os
filename = "Projedosya_1"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
kendi adınızda bir dosyayı w modunu kullanarak oluşturunuz
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
