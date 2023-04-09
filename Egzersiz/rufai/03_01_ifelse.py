
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
aci1=input("1. aciyi giriniz:")
aci2=input("2. aciyi giriniz:")

if aci1 and aci1.isdigit() and aci2 and aci2.isdigit():
    aci1=int(aci1)
    aci2=int(aci2)

aci3=180-(aci1+aci2)

if aci1==aci2 and aci1>aci3 or aci1==aci2 and aci1<aci3:
    print("Bu ucgen ikizkenardir.Bu ucgenin 3. acisi = ",aci3)  
elif aci1!=aci2 and aci2!=aci3:
    print("Bu cesitkenardir.Bu ucgenin 3. acisi = ",aci3)
else: #aci1==aci2 and aci1==aci3:
    print("Bu ucgen eskenardir.Her kenar 60 derecedir.")
