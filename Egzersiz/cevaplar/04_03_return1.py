
# """

# Faktoriyel hesabı yapan bir fonksiyon yazalım 
# fonksiyon sonucu dışarı return deyimi ile göndersin.
# print fonksiyonu ve yazdığımız faktoriyel fonksiyonunu 
# birlikte kullanıp sonucu
# ekrana yazdıralım.
# """

# def faktoriyel(sayi):
#     sonuc = 1
#     for i in range(1,sayi+1):
#         sonuc *= i
#     return sonuc

# print(faktoriyel(5))

# def faktoriyel2(sayi):
#     import math
#     return math.factorial(sayi)


# print(faktoriyel2(5))

# def faktoriyel3(sayi):
#     if sayi == 1:
#         return 1
#     else:
#         return faktoriyel3(sayi-1) * sayi

# print(faktoriyel3(5))



# # 3
# n = 6
# son = n*2-1
# sonuc = []
# for i in range(1,son+1,2):
#     print(" "*((son-i)//2),i*"#"," "*((son-i)//2))
#     sonuc.append(" "*((son-i)//2),i*"#"," "*((son-i)//2))



# n = 6
# son = (n*2-1)
# # sonuc = []
# # for i in range(1,son+1,2):
# #     print(" "*((son-i)//2),i*"#"," "*((son-i)//2))
# #     sonuc.append(" "*((son-i)//2),i*"#"," "*((son-i)//2))

# ["".join((" "*(((n_floors*2-1)-i)//2),i*"#"," "*(((n_floors*2-1)-i)//2))) for i in range(1,(n_floors*2-1)+1,2)]