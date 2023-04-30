
"""

1. gönderilen sayıların arasından en büyük üç sayıyı geri gönderen fonksiyonu yazınız
2. parametre olarak gönderilen bir metnin içinde ki büyük ve küçük harf sayılarını 
ekrana yazdıran python programını yazınız
Bonus soru 
Fonksiyon içindeki bir fonksiyona erişebilecek python kodu yazınız
"""

def outer_function():
    def inner_function():
        print("Merhaba Bera inner")
    print("Merhaba Bera outer")
    return inner_function()

outer_function()
outer_function()

