
"""

def toplam(a,b):
    print(a+b)
toplam(3,4)

yukarıdaki kod bloğundan faydalanarak 4 işlem için birbirinden farklı 4
fonksiyon yazınız
"""

def Topla(x, y):
   return x + y
 
def Cikar(x, y):
   return x - y
 
def Carp(x, y):
   return x * y
 
def Bol(x, y):
   return x / y

print("Yapılacak İşlemi Seçiniz")
print("1.Toplama")
print("2.Cıkarma")
print("3.Carpma")
print("4.Bölme")

x = int(input("1. Sayı: "))
y = int(input("2. Sayı: "))

secim=input("Bir İşlem Seçiniz Seçtiğiniz İşlemin Numarasını Yazınız")

if secim == '1':
   print(x,"+",y,"=", Toplama(x,y))

elif secim == '2':
   print(x,"-",y,"=", Cikarma(x,y))

elif secim == '3':
   print(x,"*",y,"=", Carpma(x,y))

elif secim == '4':
    print(x,"/",y,"=",Bölme(x,y))

else print("Yanlış Giriş")

