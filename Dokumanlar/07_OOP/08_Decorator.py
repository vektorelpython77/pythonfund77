# class A:
#     tur = "Sınıf Özelliği"
#     def __init__(self):
#         self.ornekOzellik = "A"
#         self.ornekMethod()
    
#     def ornekMethod(self):
#         return self.ornekOzellik

#     @classmethod # decorator
#     def sinifMethod(cls):
#         print(cls.tur)

# obj1 = A()

# import time
# def hesapZaman(fonk):
#     def icfonk(*args,**kwargs):
#         baslangic = time.time()
#         fonk(*args,**kwargs)
#         bitis = time.time()
#         print(f"{fonk.__name__} {bitis-baslangic} zamanda çalıştı")
#     return icfonk

# @hesapZaman
# def faktoriyel(sayi):
#     sonuc = 1
#     for i in range(1,sayi+1):
#         sonuc *= i
#     else:
#         print(sonuc)

# faktoriyel(5)   