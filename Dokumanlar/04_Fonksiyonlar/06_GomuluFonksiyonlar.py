"""
abs
round
all
any
ascii
repr
chr
ord
eval
exec
map
zip
filter
sorted
"""
### abs
# print(abs(-20)) # mutlak değer alımı
### round
# print(round(22/7,5)) 
### all
# # var1 = 0
# # var1 = ""
# # if var1:
# #     print("Dolu")
# # else:
# #     print("Boş")
# liste = [1,3,1,5,"ALi",[1,2,3],{1,2}]
# print(all(liste))
### any
# liste = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print(any(liste))
### ascii
# print("fıstıkçı şahap")
# print(ascii("fıstıkçı şahap")) # 'f\u0131st\u0131k\xe7\u0131 \u015fahap'
# print(ascii("f\u0131st\u0131k\xe7\u0131 \u015fahap")) # '\u015eeker' 
### repr
# print(repr("f\u0131st\u0131k\xe7\u0131 \u015fahap"))
### chr
# print(chr(350)) # Ş
## ord
# print(ord("Ş")) # 350
### eval => evaluate
# print(eval("2+5")) # 7
# print(eval(input("İşlemi Giriniz:")))
### exec => execute
# exec("a=6")
# print(a)
### map
# liste = [2,4,6,8,10]
# fonk = lambda x:x**2
# print(map(fonk,liste)) # <map object at 0x0000026BC63FAB00>
# print(*map(fonk,liste))
# # map Örnek
# tckimlikno = "10000000146"
# print(list(tckimlikno)) # ['1', '0', '0', '0', '0', '0', '0', '0', '1', '4', '6']
# print(*map(int,list(tckimlikno)))
# # print(int("0000000000000000012"))
# # print(*map(int,list("0000000000000000012")))
# # isim = "ali veli ayşe fatma"
# # print(*map(str.upper,isim))
### zip
# isimler = ["Ali","Ayşe","Fatma"]
# notlar = [90,80,70]
# print(zip(isimler,notlar)) # <zip object at 0x00000166A244E840>
# print(*zip(isimler,notlar)) # ('Ali', 90) ('Ayşe', 80) ('Fatma', 70)
# print(list(zip(isimler,notlar))) # [('Ali', 90), ('Ayşe', 80), ('Fatma', 70)]
# sozluk = {}
# sozluk.update(zip(isimler,notlar))
# print(sozluk) # {'Ali': 90, 'Ayşe': 80, 'Fatma': 70}
# print(*zip(*zip(isimler,notlar))) # unzip
############## Egzersiz Cevap
# liste =["elma","süt","soğan","patates","kıyma","portakal","yakıt"]
# fiyatlar = [20,28,30,15,300,50,20]
# fiyatlar = list(map(lambda x:x*1.20,fiyatlar)) # 1.
# print(*zip(liste,fiyatlar))  #('elma', 24.0) ('süt', 33.6) ('soğan', 36.0) ('patates', 18.0) ('kıyma', 360.0) ('portakal', 60.0) ('yakıt', 24.0) 2.
# alisverisliste = {}
# alisverisliste.update(zip(liste,fiyatlar)) # 3.
# print(alisverisliste) # {'elma': 24.0, 'süt': 33.6, 'soğan': 36.0, 'patates': 18.0, 'kıyma': 360.0, 'portakal': 60.0, 'yakıt': 24.0}
### filter
# liste = [1,2,3,4,5,6,7,8,9,10]
# metin = "Vektorel Bilisim"
# def buyukharfmi(karakter):
#     return karakter.isupper()
# print(filter(buyukharfmi,metin)) # <filter object at 0x0000019A27FBAA40>
# print(*filter(buyukharfmi,metin)) # V B
# ciftmi = lambda x:x%2==0
# print(*filter(ciftmi,liste)) # 2 4 6 8 10
### sorted
# liste = [5,6,10,8,67,45,65,12]
# print("sort fonksiyonu çıktısı:",liste.sort()) # None
# print("listenin sıralanmış hali:",liste) # [5, 6, 8, 10, 12, 45, 65, 67]
# liste = [5,6,10,8,67,45,65,12]
# print("sorted fonksiyonu çıktısı:",sorted(liste)) # [5, 6, 8, 10, 12, 45, 65, 67]
# print("listenin son hali:",liste) # [5, 6, 10, 8, 67, 45, 65, 12]
# """
# sort fonksiyonu çıktısı: None
# listenin sıralanmış hali: [5, 6, 8, 10, 12, 45, 65, 67]
# sorted fonksiyonu çıktısı: [5, 6, 8, 10, 12, 45, 65, 67]
# listenin son hali: [5, 6, 10, 8, 67, 45, 65, 12]
# """
