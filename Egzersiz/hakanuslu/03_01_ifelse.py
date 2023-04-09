
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
aci1 = int()(input("Üçgenin ilk açısını girin: "))
aci2 = int(input("Üçgenin ikinci açısını girin: "))

if (aci1==60  and aci2==60):
    print("Eşkenar üçgen")
elif (aci1 == aci2 ):
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")
