"""
1. tanımlama
2. Yardımcı Fonksiyonlar
"""
#####set
# kume1 = {1,2,3}
# kume2 = set()
# print(type(kume1)) #<class 'set'>
# print(type(kume2)) #<class 'set'>
#########
liste1 = [1,2,3,4,5,1,1,1,11,1,1,2,2,2,2,1,1,1,1,1,2,2,2]
liste2 = [4,5,6,7,8,7,34,43,4,4,5,5,4,]
kume1 = set(liste1)
kume2 = set(liste2)
print(kume1) #{1, 2, 3, 4, 5, 11}
######## Yardımcı Fonksiyonlar
print(kume1.intersection(kume2)) # {4, 5}
print(kume1.difference(kume2)) # {11, 1, 2, 3}
print(kume1.symmetric_difference(kume2)) # {1, 2, 3, 6, 7, 8, 11, 34, 43}

