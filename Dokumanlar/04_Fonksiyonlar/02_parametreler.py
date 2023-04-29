"""
1. isimli parametre tanımı
2. args yöntemi
3. kwargs yöntemi
"""
############### 1
def topla(a,b):
    print(f"{a} + {b} = {a+b}")
topla(2,3)
topla(b=2,a=4)
topla(3,b=2)


def topla(a,b,c=0):
    print(a+b+c)
topla(2,3)
topla(b=2,a=4)
topla(3,b=2,c=3)