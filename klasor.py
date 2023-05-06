import os
filename = "04_04_Egzersiz2"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
bir dörtgenin iki kenarını parametre olarak alan bir fonksiyonun
bu dörtgenin kare mi yoksa dikdörtgen mi olduğunu söylemesini 
ve alanını hesaplaması istenmektedir. Bu işlemi gerçekleştiren 
fonksiyonu yazınız
Örnek Çıktı: Dikdörtgenin Alanı: 12 cm2
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
