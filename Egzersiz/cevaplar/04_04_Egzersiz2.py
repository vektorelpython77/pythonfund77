
"""
istenilen uzunlukta ve aşağıdaki kriterleri sağlayan şifre üreten
fonksiyonu yazınız
1. en az bir küçük harf olmalıdır
2. en az bir büyük harf olmalıdır
3. en az bir rakam olmalıdır
4. en az bir noktalama işareti olmalıdır

from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import random as rnd

yukarıdaki kütüphanelerden faydalanabilirsiniz.
"""
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import random as rnd
def sifrekontrol(sifre):
    bHarf = kHarf = rakam = noktalama = False
    for item in sifre:
        if item.isalpha():
            if item.isupper():
                bHarf = True
            else:
                kHarf = True
        elif item.isdigit():
            rakam = True
        elif item in punctuation:
            noktalama = True
    return bHarf and kHarf and rakam and noktalama

def sifreUretici(n):
    liste = [ascii_lowercase,ascii_uppercase,digits,punctuation]
    result = []
    while not sifrekontrol("".join(result)):
        for i in range(n):
            result.append(rnd.choice(rnd.choice(liste)))
    else:
        return "".join(result)

print(sifreUretici(12))



def yesFonk(uzunluk):
    import random
    import string
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = random.sample(characters, uzunluk)
    yes = "".join(password)
    return yes

def yesFonk(uzunluk):
    import random
    import string
    password = ""
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    while not sifrekontrol("".join(password)):
        password = random.sample(characters, uzunluk)
    else:
        yes = "".join(password)
    return yes
# print(yesFonk())
sayi = 0
sayi2 = 0
for item in range(20):
    sifre = yesFonk(12)
    sifre2 = sifreUretici(12)
    if sifrekontrol(sifre):
        sayi+=1
    else:
        print(sifre)
    if sifrekontrol(sifre2):
        sayi2 += 1

print(sayi)
print(sayi2)



def yesFonk(uzunluk):
    import random
    import string
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    while not sifrekontrol("".join(password)):
        password = random.sample(characters, uzunluk)
    else:
        yes = "".join(password)
    return yes




def sifrekontrol(sifre):
    bHarf = kHarf = rakam = noktalama = False
    for item in sifre:
        if item.isalpha():
            if item.isupper():
                bHarf = True
            else:
                kHarf = True
        elif item.isdigit():
            rakam = True
        elif item in punctuation:
            noktalama = True
    return bHarf and kHarf and rakam and noktalama

def find_uniq(arr):
    kume = set(arr) # [ 1, 1, 1, 2, 1, 1 ] => {1,2}
    for item in kume:
        if arr.count(item) == 1: # [ 1, 1, 1, 2, 1, 1 ].count(2) == 1
            n = item
    return n  
    return int(item for item in set(arr) if arr.count(item) == 1)

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))