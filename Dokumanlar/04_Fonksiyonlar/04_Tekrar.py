def merhabaDe(): # Tanımlama
    print("Merhaba")
a = 2
merhabaDe() #Çağırma

# def topla(a,b):
#     print(a+b)

# topla(2,3)
# topla(5,7)
##########################################

# def topla(a,b,c=0):
#     print(a+b+c)

# topla(2,3)
# topla(2,3,5)
# print("ali","veli") # ali veli
# print("ali","veli",sep="-") # ali-veli
##############################################
# def topla(a,b,c=0):
#     print(a+b+c)

# topla(2,3)
# topla(3,5,2)
# topla(b=2,a=4,c=4)
# topla(c=2,b=4,a=4)
##############################################
# def topla(a,b,c=0):
#     print(a+b)
    
# topla(b=4,a=4)
##############################################
# def topla(*args):
#     print(type(args))

# topla()
# topla(1,2,3,4)
# topla(1,2)
# topla(1,2,3,34,5,6,7,8,)

# def topla(*args): # (1,2,3,4,5)
#     sonuc = 1
#     for item in args:
#         sonuc = sonuc * item
#     print(sonuc)
# topla(1,2,3,4,5,6)
# topla()
# topla(23,262,256,260,2852,)

###########################################

def topla(**kwargs):
    print(type(kwargs))
    print(kwargs)

topla()
topla(a=2)
topla(a=2,b=2)

###########################################

# def konus(**kwargs):
#     for key,value in kwargs.items():
#         if key=="selam":
#             print("Merhaba",value)
#         if key=="sor":
#             print(value,"?")
# konus(selam="İbrahim",sor="İyi misin")

###########################################

# def topla1(a,b):
#     print("Topla 1 fonksiyonu içinden:",a+b)

# def topla2(a,b):
#     return "Topla 2 fonksiyonu içinden:" + str(a+b)

# topla1(2,3)
# sonuc = topla2(2,3)
# print(sonuc)

#########################################

def kare(x):
    return x**2

def kup(y):
    return y**3

def topla(k,j):
    return k+j

a = kare(5)
b = kup(3)
print(topla(a,b))
print(topla(kare(5),kup(3)))


