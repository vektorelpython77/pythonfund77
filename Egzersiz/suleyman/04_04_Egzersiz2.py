
"""
bir dörtgenin iki kenarını parametre olarak alan bir fonksiyonun
bu dörtgenin kare mi yoksa dikdörtgen mi olduğunu söylemesini 
ve alanını hesaplaması istenmektedir. Bu işlemi gerçekleştiren 
fonksiyonu yazınız
Örnek Çıktı: Dikdörtgenin Alanı: 12 cm2
"""


def dortgen(a,b):
    alan = a*b
    return f"{'Kare' if a==b else 'Dikdörtgen'} in alanı {alan} cm2"

print(dortgen(5,4))