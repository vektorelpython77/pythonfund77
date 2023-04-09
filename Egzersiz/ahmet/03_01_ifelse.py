
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
a=(input("1. açıyı giriniz."))
b=(input("2. açıyı giriniz."))
c=180-(a+b)
if acibir and acibir.isdigit() and aciiki and aciiki.isdigit():
 acibir=int(acibir)
 b=int(aciiki)

if(a == b== c== 60):
    print("Eşkenardır")
elif(a==b or a==b or a==b):
    print("İkizkenar Üçgendir")
elif(c>90):
    print("Geniş kenar üçgen")
else:
    print("girdiginiz deger yanlıs.")