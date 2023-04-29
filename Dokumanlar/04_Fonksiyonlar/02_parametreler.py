"""
1. isimli parametre tanımı
2. args yöntemi
3. kwargs yöntemi
"""
############### 1
# def topla(a,b):
#     print(f"{a} + {b} = {a+b}")
# topla(2,3)
# topla(b=2,a=4)
# topla(3,b=2)


# def topla(a,b,c=0):
#     print(a+b+c)
# topla(2,3)
# topla(b=2,a=4)
# topla(3,b=2,c=3)
##################################
# def topla(a,b,c=0):
#     print(a,b,c)

# topla(1,2)
# #     a,b
# topla(1,2,3)
# #     a,b,c
################################## 2. args arguments

# def fonk(*args):
#     print(type(args))
#     res = 0
#     for i in args:
#         res += i
#     print(res)
# fonk()
# fonk(1,2,3)
# fonk(2,3,1,2,2,3,2,2,2,1,1,2)


#################################### 3. kwargs keyword adrguments
# def fonk(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# fonk(adi="İbrahim",soyadi="Ediz")
# fonk()
# fonk(adi=İbrahim)


######################### Birlikte kullanım

# def fonk(a,b,*args,**kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)

# fonk(1,2,3,4,5,6,7,8,9,son=10)
# 1 2
# (3, 4, 5, 6, 7, 8, 9)
# {'son': 10}

################## örnek
# def bilgi(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# bilgi(Adı="İbrahim",Soyadı="EDİZ")
# bilgi(Adı="İbrahim",Soyadı="EDİZ",eposta="edizdesign@gmail.com")
# bilgi(Adı="İbrahim",Soyadı="EDİZ",Şehir="Ankara")
# bilgi(Adı="İbrahim",Soyadı="EDİZ",Ders="Python")
# bilgi(Adı="İbrahim",Soyadı="EDİZ")