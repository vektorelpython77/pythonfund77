
"""
bir dörtgenin iki kenarını parametre olarak alan bir fonksiyonun
bu dörtgenin kare mi yoksa dikdörtgen mi olduğunu söylemesini 
ve alanını hesaplaması istenmektedir. Bu işlemi gerçekleştiren 
fonksiyonu yazınız
Örnek Çıktı: Dikdörtgenin Alanı: 12 cm2
"""
def dortgen(a,b):
    alan = a*b
    if a != b:
        return f"Dikdörtgenin Alanı {alan} cm2"
    else:
        return f"Karenin Alanı {alan} cm2"
print(dortgen(5,5))
print(dortgen(6,9))



