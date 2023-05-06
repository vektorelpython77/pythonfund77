
"""
bir dörtgenin iki kenarını parametre olarak alan bir fonksiyonun
bu dörtgenin kare mi yoksa dikdörtgen mi olduğunu söylemesini 
ve alanını hesaplaması istenmektedir. Bu işlemi gerçekleştiren 
fonksiyonu yazınız
Örnek Çıktı: Dikdörtgenin Alanı: 12 cm2
"""

def dörtgen(a,b):
    return(a*b)

if a == b:
    return("bu bir dörtgendir.")

if a > b or a < a:
    return("bu bir dikdörtgendir.")