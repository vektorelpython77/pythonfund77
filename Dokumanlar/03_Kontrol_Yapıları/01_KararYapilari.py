# a = 2
# if a == 2: # True or False
#     print("a 2 dir") # indentitaion
##################
"""
1. Karşılaştırma Operatörleri
    * == eşit mi ?
    * != eşit değil mi ?
    * >= Büyük eşit mi ?
    * <= Küçük eşit mi ?
    * > büyük mü ?
    * < küçük mü ?
2. Mantıksal Operatörler
    * not 
    * and 
    * or
3. Kimlik Operatörü
    * is
    * is not 
4. Üyelik Operaötür
    * in 
    * not in 
5. Aritmetik Operatörler
    * +,-,*,/
    * // Bölümün tam kısmı 
    * % Modulus
    * ** Kuvvet
"""
###############################
# var1,var2,var3,var4,var5,var6 = 1,"",[],(),{},set()
# if var1:
#     print("Dolu")
# else:
#     print("Boş")
###############################

# yas = input("Yaşınızı Giriniz:")
# if yas and yas.isdigit():
#     yas = int(yas)
#     if yas > 12:
#         print("Oyun Oynayabilir")
#     else:
#         print("Oyun Oynayamaz")
#     print("Giriş Yapıldı")
# else:
#     print("Giriş Yapmalısınız ya da Değer Hatası") 
###################################
# var1 = 259
# var2 = 259.0
# print(var1 == var2)
# print(var1 is var)
####################
# var1 = 350   # -5 25
# var2 = 350
# print(id(var1),id(var2))
# print(var1 == var2) # True
# print(var1 is var2)
#####################
# liste = [1,2,3,4,5,6]
# if 5  in liste:
#     print("içerde")
# var1 = {"1":"Bir","2":"İki"}
# if "if" in var1:
#     print("içerir")
############################## Elif
"""
Notlar:
85-100 AA
70-84 BB
55-69 CC
"""
##########################
_not = input("Notunuzu Giriniz:")
# _not = 75
if _not and _not.isdigit():
    _not = int(_not)
    if 85 <= _not <= 100: #  _not >= 85 and _not <= 100
        print("AA")
    elif 70 <= _not <= 84:
        print("BB")
    elif 55 <= _not <= 69:
        print("CC")
    else:
        print("Yanlış Not")
            
