# a = 5 #global
# def fonk():
#     a = 3 #local
#     print("Fonksiyon içerisinden:",a)
# print("Fonksiyon çalışmadan önce: ",a) # 5
# fonk() # 3
# print("Fonksiyon çalıştıktan sonra:",a) # 5

# a = 5 #global
# def fonk():
#     global a ##########################
#     a = 3 #global
#     print("Fonksiyon içerisinden:",a)
# print("Fonksiyon çalışmadan önce: ",a) # 5
# fonk() # 3
# print("Fonksiyon çalıştıktan sonra:",a) # 3

a = 5
def fonk():
    a = 3
    print("1. Fonksiyon içerisinden:",a) # 3
    def icfonk():
        a = 2
        print("İç Fonksiyon içerisinden:",a) # 2
    icfonk()
    print("2. Fonksiyon içerisinden:",a) # 3
print("Fonksiyon çalışmadan önce: ",a) # 5
fonk() 
print("Fonksiyon çalıştıktan sonra:",a) # 5

#####################################
print("#"*30)
print("Global kullanırsak")
a = 5
def fonk():
    global a ############################ 
    a = 3 # global
    print("1. Fonksiyon içerisinden:",a) # 3
    def icfonk():
        a = 2
        print("İç Fonksiyon içerisinden:",a) # 2
    icfonk()
    print("2. Fonksiyon içerisinden:",a) # 3
print("Fonksiyon çalışmadan önce: ",a) # 5
fonk() 
print("Fonksiyon çalıştıktan sonra:",a) # 3
#######################################
print("#"*30)
print("iç fonksiyonda Global kullanırsak")
a = 5 # global
def fonk():
    a = 3 # local
    print("1. Fonksiyon içerisinden:",a) # 3
    def icfonk():
        global a ############################ 
        a = 2 # global
        print("İç Fonksiyon içerisinden:",a) # 2
    icfonk()
    print("2. Fonksiyon içerisinden:",a) # 3
print("Fonksiyon çalışmadan önce: ",a) # 5
fonk() 
print("Fonksiyon çalıştıktan sonra:",a) # 2
#############################################
print("#"*30)
print("nonlocal")
a = 5 # global
def fonk():
    a = 3 # alınan değer
    print("1. Fonksiyon içerisinden:",a) # 3
    def icfonk():
        nonlocal a ############################ 
        a = 2 # bir üst fonksiyon içindeki a
        print("İç Fonksiyon içerisinden:",a) # 2
    icfonk()
    print("2. Fonksiyon içerisinden:",a) # 2
print("Fonksiyon çalışmadan önce: ",a) # 5
fonk() 
print("Fonksiyon çalıştıktan sonra:",a) # 5