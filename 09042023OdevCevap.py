# """
# 1. Aşağıdaki şekli ekrana yazdıran python kodunu yazınız
# #
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # #
# # # # # # 
# # # # # 
# # # # 
# # # 
# #
# """
# # Don't Repeat Yourself
# # We Enjoy Texting

# karakter = "# ",
# adim = 6
# for i in range(1,adim): # 1 2 3 4 5 
#     print(i*karakter)
# for i in range(adim,0,-1): # 6 5 4 3 2 1
#     print(i*karakter)


# """
# 2. 
# 1 ile 150 sayıları arasındaki sayılardan 15'e tam bölünebilen 
# sayıların listesini ekrana yazdıran python kodunu yazınız
# """
# for i in range(1,151):
#     if i % 15 == 0:
#         print(i,end=" ")
# # print(*liste)
# # # for item in liste:
# # #     print(item,end=" ")
# """
# 3.
# fibanocci serisinde verilen sınıra kadar seri elemanlarını ekrana 
# yazdıran programı yazınız
# """
# a = 1
# b = 1
# print(a)
# print(b)
# for i in range(10):
#     c = a+b
#     print(c)
#     a = b
#     b = c
#########################
# a = b = 1
# print(a,b,sep="\n")
# for i in range(10):
#     print(a+b)
#     a,b = b,a+b
####################################
"""
1. Başla
2. sayıyı oku
3. sayacı sıfır tanımla
4. sayacı 1 arttır
5. eğer sayının sayaca bölümünden kalan 0 ise 9 adıma git
6. eğer sayı sayaca eşitse 8. adıma git
7. eğer sayı sayaca eşit değilse 4. adıma git
8. Sayı Asaldır yaz 10. adıma git
9. Sayı Asal Değildir Yaz
10. Bitir
"""
# sayi = input("Sınır Sayıyı Giriniz:")
# if sayi and sayi.isdigit():
#     sayi = int(sayi)
#     for j in range(2,sayi):
#         for i in range(2,j):
#             if j % i == 0:
#                 # print(f"Sayı Asal Değildir {j}")
#                 break
#         else:
#             print(f"Sayı Asaldır {j}")



# liste = [i for i in range(0,101)]

# primeList = [2,3,4,5,6,7,8,9]
# for sayi in primeList: # 2 3 4 5 6 7 8 9
#     for i in range(0,101,sayi): # 3 6 9 12 15
#         if i in liste:
#             liste.remove(i)
# else:
#     liste.remove(1)
#     liste.extend((2,3,5,7))
#     liste.sort()
#     print(liste)

"""
sayısal loto oyununda 1,49 sayıları arasındaki sayılardan 
6 adet sayının seçilmesi gerekmektedir.
1. Alternatif 
from random import randint
randint(1,49)
2. Alternatif
from random import choice
liste = [i for i in range(1,50)]

yukarıdaki kod bloklarında faydalanarak 
istenilen sayıda sayısal loto kolonu oynayan python kodunu 
yazınız
ipucu while ve for döngüleri birlikte kullanılmaktadır. 
"""



