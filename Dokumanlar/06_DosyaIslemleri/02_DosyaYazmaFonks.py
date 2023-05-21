"""
write
writelines
"""
adres = "Projeler\Dosyalamaİslemleri\ornek.csv"
kip="w+"
dosya = open(adres,kip,encoding="UTF-8")
bilgi = "Ali;Veli;123\n"
for i in range(8):
    dosya.write(bilgi)
liste = []
for i in range(9):
    liste.append(str(i) + ";" + bilgi)
dosya.writelines(liste)