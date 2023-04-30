
"""

1. gönderilen sayıların arasından en büyük üç sayıyı geri gönderen fonksiyonu yazınız
2. parametre olarak gönderilen bir metnin içinde ki büyük ve küçük harf sayılarını 
ekrana yazdıran python programını yazınız
Bonus soru 
Fonksiyon içindeki bir fonksiyona erişebilecek python kodu yazınız
"""
# 1. gönderilen sayıların arasından en büyük üç sayıyı geri gönderen fonksiyonu yazınız
def sirala(*args):
    # liste = list(args)
    # liste.sort(reverse=True)
    # return liste[0:3]
    return sorted(args,reverse=True)[0:3]


# 2. parametre olarak gönderilen bir metnin içinde ki büyük ve küçük harf sayılarını 
# ekrana yazdıran python programını yazınız

def dokum(metin):
    buyuk = kucuk = 0
    for item in metin:
        if item.isalpha():
            if item.isupper():
                buyuk+=1
            else:
                kucuk+=1
    print(buyuk,kucuk)

def dokum(metin):
    # print(len([metin[i] for i in range(len(metin)) if metin[i].isupper()]))
    print(len([item for item in metin if item.isupper()]))
    print(len([item for item in metin if item.islower()]))
# Bonus
# def outer_function():
#     def inner_function():
#         print("Merhaba Bera inner")
#     print("Merhaba Bera outer")
#     return inner_function()

# outer_function()
# outer_function()

