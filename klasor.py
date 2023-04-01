import os
filename = "02_02_str"
liste = os.listdir("Egzersiz/")
for item in liste:
    with open(f"Egzersiz/{item}/{filename}.py","w+") as dosya:
        metin = """
\"\"\"
    isim = input("İsminizi Giriniz:")
    soyisim = input("Soyisminizi Giriniz:)
    var1 = ?"{????}",?"{???????}","Ankara","555"
    print(";".????.(?????))

    yukarıdaki kod parçacığı içerisindeki ? ile gösterilen alanları uygun bilgilerle
    doldurunuz
\"\"\"
"""
        dosya.write(metin)
# TODO veri tabanı bağlantrısı eklenecek 
