
"""
bir dörtgenin iki kenarını parametre olarak alan bir fonksiyonun
bu dörtgenin kare mi yoksa dikdörtgen mi olduğunu söylemesini 
ve alanını hesaplaması istenmektedir. Bu işlemi gerçekleştiren 
fonksiyonu yazınız
Örnek Çıktı: Dikdörtgenin Alanı: 12 cm2
"""

def sekil(a,b):
    return a*b

    if a>b or b>a:
print("Dikdortgenin Alanı:",sekil(3,4))
else:
    print("Karenin Alanı:",sekil(3,4))