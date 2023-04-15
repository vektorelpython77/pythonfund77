
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

# from random import randint
# buyukListe = []
# for j in range(int(input("Kolon Sayısını Giriniz:"))):
#     liste = []
#     for i in range(6):
#         sayi = randint(1,49)
#         while sayi in liste:
#             sayi = randint(1,49)
#         liste.append(sayi)
#     else:
#         liste.sort()
#         buyukListe.append(liste)
# else:
#     print(*buyukListe,sep="\n")




# from random import choice
# sayiListe = [i for i in range(1,50)]
# buyukListe = []
# for j in range(int(input("Kolon Sayısını Giriniz:"))):
#     liste = []
#     for i in range(6):
#         sayi = choice(sayiListe)
#         while sayi in liste:
#             sayi = choice(sayiListe)
#         liste.append(sayi)
#     else:
#         liste.sort()
#         buyukListe.append(liste)
# else:
#     print(*buyukListe,sep="\n")


# from random import sample
# for j in range(int(input("Kolon Sayısını Giriniz:"))):
#     print(sample([i for i in range(1,50)],6))


