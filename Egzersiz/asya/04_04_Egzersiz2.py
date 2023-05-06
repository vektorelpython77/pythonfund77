
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
password_length = 12
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_characters = lowercase_letters + uppercase_letters + digits + symbols
password = ''.join(random.sample(all_characters, password_length))
print(password)




def find_uniq(arr):
    kume = set(arr) 
    for item in kume:
        if arr.count(item) == 1: 
            n = item
    return n  

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))