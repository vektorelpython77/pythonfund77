
"""

Faktoriyel hesabı yapan bir fonksiyon yazalım 
fonksiyon sonucu dışarı return deyimi ile göndersin.
print fonksiyonu ve yazdığımız faktoriyel fonksiyonunu 
birlikte kullanıp sonucu
ekrana yazdıralım.
"""
def factorial(n):
    f=1
    for i in range (1,n+1):
        f*=i
    return f
print(factorial(5))