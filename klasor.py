import os
filename = "OOPExercise_3"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+",encoding="UTF-8") as dosya:
        metin = """
\"\"\"
Bir şarküteri  ürettiği ürünleri yapay zeka ile 
ilişkilendirerek bir proje yapmak istemektedir.
Bu işlem için bazı kurallar belirlenmesi gerekmiştir. İlk kuralın 
her ürüne çeşidine ait bir URUNID numarası olduğu bilinmektedir. 
Yazılımcı olarak bu numaranın tüm sınıflarda olmasını sağlayacak 
durumu yazınız.

\"\"\"

"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı


# https://codeshare.io/eVn8ml
