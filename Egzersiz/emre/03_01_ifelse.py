
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
x=(input('Birinci açıyı giriniz.'))
y=(input('İkinci açıyı giriniz.'))

if x and x.isdigit() and y and y.isdigit():
    x=int(x)
    y=int(y)
    
z=180-(x+y)
if(x == y== z== 60):
    print("Eşkenar")
elif(x==y or y==z or x==z):
    print("İkizkenar Üçgen")
elif(z==90):
    print("Dik Üçgen")
elif(z>90):
    print("Geniş kenar üçgen")
else:
    print("Dar açılı üçgen")