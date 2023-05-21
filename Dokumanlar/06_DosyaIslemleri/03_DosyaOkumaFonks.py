"""
read => str
realine => satır satır str
readlines => tümünü okur list
"""
adres = "Projeler\Dosyalamaİslemleri\ornek.csv"
kip="r+"
dosya = open(adres,kip,encoding="UTF-8")
print("#"*15,"read","#"*15)
print(dosya.read(10)) # boş bırakılırsa tümünü okur
print("#"*15,"read","#"*15)
print("#"*15,"readline","#"*15)
print(dosya.readline())
print(dosya.readline(2))
print(dosya.readline())
print("#"*15,"readline","#"*15)
print("#"*15,"readlines","#"*15)
print(dosya.readlines())
print("#"*15,"readlines","#"*15)