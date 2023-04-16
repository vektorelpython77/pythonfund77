"""
1. range
2. for 
3. while
4. break,else,continue
"""
##### range
# print(*range(0,6)) # 0 1 2 3 4 5
# print(*range(6)) # 0 1 2 3 4 5
# print(*range(6,0,-1)) # 6 5 4 3 2 1
# print(*range(5,30,5)) # 5 10 15 20 25
###################### for
# for i in range(6):
#     print(i*"* ")
# var1 = "Vektorel"
#       01234567
# var1[0] => V
########
# for i in range(len(var1)): # 0 1 2 3 4 5 6 7
#     print(var1[i])
#########
# for ch in var1: # V e k t o r e l
#     print(ch)
# var1 = """
# Rapor: Hindistan, 2026 yılına kadar dünyanın 
# en büyük ikinci güneş fotovoltaik üreticisi olabilir
# """
# # for item in var1:
# #     if item.isupper():
# #         print(item)

# print(set([item for item in var1 if item.islower()]))
# import collections as col
# print(col.Counter(var1))


# https://codeshare.io/MNLMDy
####################### while
# anahtar = 1
# while anahtar == 1:
#     menu = """
#     1.Toplama
#     2.Çıkarma
#     3.Çıkış
#     İşlem Seçiniz:
#     """
#     giris = input(menu)
#     if giris == "3":
#         anahtar = 0
#     if giris == "2":
#         print("Döngü Kırıldı")
#         break
#     if giris == "1":
#         print("1")
#         continue
#         print("1a") # yazmaz
# else:
#     print("İyi Günler")

# adim = 0
# while True:
#     adim += 1  # adim = adim + 1
#     if adim == 2:
#         continue
#     if adim == 5:
#         break
#     print(adim)

# sayi = int(input("Sayıyı Giriniz"))
# basamak  = 10
# adim = 0
# while sayi != 0:
#     print(sayi%basamak*(basamak**(adim)))
#     adim += 1
#     sayi = sayi // basamak

# sayi = input("Sayıyı Giriniz") # 128258
# dizi = list(sayi)
# print(dizi) # ['1', '2', '8', '2', '5', '8']
# dizi.reverse()
# print(dizi) # ['8', '5', '2', '8', '2', '1']
# adim = 0
# for i in range(len(dizi)):
#     print(int(dizi[i])*10**i)

