""" 
return 
yield 
""" 

def fonk1(a,b):
    print(a+b)

# def fonk2(a,b):
#     return a+b
#     print("ÇALIŞMAZ")

# fonk1(2,3)
# print(fonk1(2,3)) #None
# print(fonk2(2,3)) #5 çünkü return sayıları dışarı gönderdi


# def fonk(a,b):
#     return a,b,a+b

# print(fonk(2,3))
# sonuc = fonk(2,3) # (2, 3, 5)
# print(f"{sonuc[0]} + {sonuc[1]} = {sonuc[2]}")

def fonk(metin,sayi):
    import random
    metin = list(metin)
    for i in range(sayi):
        random.shuffle(metin)
        yield "".join(metin)

print(fonk("Galatasaray",5)) # <generator object fonk at 0x7f93a6151030>
# print(range(1,2)) # range(1, 2)
# print(*range(1,5))  # 1 2 3 4
# print(*fonk("Galatasaray",5),sep="\n")

for item in fonk("Galatasaray",5):
    print(item)

from string import ascii_lowercase,ascii_uppercase,digits,punctuation
print(ascii_lowercase,ascii_uppercase,digits,punctuation,sep="\n")
import random
print(random.choice(ascii_lowercase))

"""
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
"""