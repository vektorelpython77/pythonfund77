
"""
bir dörtgenin iki kenarını parametre olarak alan bir fonksiyonun
bu dörtgenin kare mi yoksa dikdörtgen mi olduğunu söylemesini 
ve alanını hesaplaması istenmektedir. Bu işlemi gerçekleştiren 
fonksiyonu yazınız
Örnek Çıktı: Dikdörtgenin Alanı: 12 cm2
"""


a = int(input("a değeri:"))
b= int(input("b değeri:"))

if a==b:
    def alan(a,b):
    return a*b
print("Gönderilen a b değerleri karenin kenarlardır.Karenin alanı =",alan(6,6))

elif a!=b:
    def alan(a,b):
    return a*b
print("Gönderilen a b değerleri dikdörtgenin kenarlardır.Dikdörtgenin alanı =",alan(6,4))


