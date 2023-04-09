
"""
iki açısı girilmiş olan
bir üçgenin tipini tespit eden programı yazınız
"""
A=input("1. açı:");print(A.isdigit())
B=input("2. açı:");print(B.isdigit())
C=180-A.isdigit()-B.isdigit();print(C)
if (A.isdigit()==B.isdigit()==C==60):
    print("Eşkenar Üçgen")
    print("Çeşit Üçgen")

