
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

import random
import string
uzunluk = int(input('Şifre uzunluğunu giriniz : '))
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
password = random.sample(characters, uzunluk)
yes = "".join(password)
print(yes)
###

def yesFonk():
    import random
    import string
    uzunluk = int(input('Şifre uzunluğunu giriniz : '))
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = random.sample(characters, uzunluk)
    yes = "".join(password)
    return yes
print(yesFonk())

##########

def find_uniq(arr):
  a, b = set(arr)
  return a if arr.count(a) == 1 else b
print(find_uniq[1,1,1,2,1,1])