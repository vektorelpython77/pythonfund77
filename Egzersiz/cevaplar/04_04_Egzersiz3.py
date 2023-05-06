
"""
parametre olarak gönderilen bir liste içerisindeki 
tüm çift sayıların toplamını return deyimi ile dönen fonksiyonu 
yazınız. 
Fonksiyonun çıktısını ekrana yazmasını fonksiyonu print
fonksiyonu içerisinde çalıştırarak sağlayınız
print(fonk(....)) gibi
"""

# FAIL First Attempt in Learning

def fonk(liste):
    # listeYeni = [item for item in liste if item %2 ==0]
    # if listeYeni:
    #     result = 1
    #     for item in listeYeni:
    #         result += item
    #     return result
    # else:
    #     return 0
    return sum([item for item in liste if item % 2 == 0])

import unittest
testC = unittest.TestCase()
print(testC.assertEqual(fonk([1,2,3,4]), 6))