"""
lambda tek satırlık fonksiyon
"""

# def fonk(a):
#     a = 2*a
#     a = a/5
#     return a**2
# print(fonk(2))
# fonk1 = lambda a:((2*a)/5)**2
# print(fonk1(2))

# def fonk(a,b):
#     return a+b
# print(fonk(2,3))
# fonk1 = lambda a,b:a+b
# print(fonk1(2,3))

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {item:alfabe.index(item) for item in alfabe} 

# {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 
# 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'ö': 18, 'p': 19, 'r': 20,
#  's': 21, 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27, 'z': 28}
print(cevrim)
fonk = lambda x:cevrim.get(x.lower()[0])
print(fonk("Çiğdem")) # Çiğdem => çiğdem => ç => çevrim.get("ç") => 3
######################## parametre=> lower => [0] => get => sonuç

isimListe = ["Ali","Ayşe","Şermin","Kamil","Sevim","Çiğdem","Ceren"]
isimListe.sort() # ['Ali', 'Ayşe', 'Ceren', 'Kamil', 'Sevim', 'Çiğdem', 'Şermin']
print(isimListe)
print(sorted(isimListe,key=fonk)) 
# ['Ali', 'Ayşe', 'Ceren', 'Çiğdem', 'Kamil', 'Sevim', 'Şermin']
