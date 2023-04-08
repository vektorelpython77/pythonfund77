#### Plan
"""
1. Tanımlama
2. Erişim
3. Güncelleme,Silme,Ekleme
4. Yardımcı Fonksiyonlar
"""
##### 1. Tanımlama
sozluk = {}
print(type(sozluk)) # <class 'dict'>
sozluk = {"1":"Bir"}
#         key: value
#### key için str,tuple ve numerik 
#### value için tüm veri tipleri kullanılabilir
##### 2. Erişim
sozluk = {"1":"Bir","2":"İki",1:"Bir"}
print(sozluk["1"])
print(sozluk[1