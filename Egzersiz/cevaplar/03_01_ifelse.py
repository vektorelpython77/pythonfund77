
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
aci1 = input("1. Açıyı Giriniz:")
aci2 = input("2. Açıyı Giriniz:")
if (aci1 and aci2) and (aci1.isdigit() and aci2.isdigit()):
    aci1,aci2 = int(aci1),int(aci2)
    aciListe = [180-(aci2+aci1),aci1,aci2] # [60,60,60]
    if sum(aciListe) == 180:
        aciKume  = set(aciListe) # {60}
        if len(aciKume) == 2: 
            print("İkizkenar Üçgen")
        elif len(aciKume) == 3:
            print("ÇeşitKenar Üçgen")
        elif len(aciKume) == 1:
            print("Eşkenar Üçgen") # OK
        if 90 in aciKume:
            print("Dik Üçgen") 
        

