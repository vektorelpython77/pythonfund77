import os
filename = "OOPExercise_2"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
Elimizde kare,diktörgen ve ücgen levhalar var
Bu levhaları üzerinde işlemler gerçekleştiriyoruz.
Bizim için bu levhaların üçünün de ortak özelliklerini ve fonksiyonlarını bir arada
tutabilecek bir sınıf oluşturmanı istiyoruz. Sınıfın isminin Cokgen olmasını bekliyoruz
özellikler ve metotlar sana kalmış...
başarılar
\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
