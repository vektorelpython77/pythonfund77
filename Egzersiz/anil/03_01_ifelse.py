
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
if(x == y== z== 60):
    print("Eşkenar")
elif(x==y or y==z or x==z):
    print("İkizkenar Üçgen")
elif(z>90):
    print("Geniş kenar üçgen")
else:
    print("YANLIŞ DEĞER GİRDİNİZ.")