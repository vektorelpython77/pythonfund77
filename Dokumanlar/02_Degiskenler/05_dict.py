#### Plan
"""
1. Tanımlama
2. Erişim
3. Güncelleme,Silme,Ekleme
4. Yardımcı Fonksiyonlar
"""
##### 1. Tanımlama
# sozluk = {}
# print(type(sozluk)) # <class 'dict'>
# sozluk = {"1":"Bir"}
#         key: value
#### key için str,tuple ve numerik 
#### value için tüm veri tipleri kullanılabilir
##### 2. Erişim
# sozluk = {"1":"Bir","2":"İki",1:"Bir"}
# print(sozluk["1"])
# print(sozluk[1])
## get
# sozluk = {"1":"Bir","2":"İki",1:"Bir"}
# print(sozluk.get("1"))
# print(sozluk.get(2)) # anahtar hatası almamak için get fonksiyonunu kullanmak 
# print(sozluk["Jamiryo"])

## setdefault
# sozluk = {"1":"Bir","2":"İki",1:"Bir"}
# print(sozluk.setdefault("1","One"),sozluk)
# # anahtar , eklenecek değer
# # Bir {'1': 'Bir', '2': 'İki', 1: 'Bir'}
# print(sozluk.setdefault("3","Üç"),sozluk)
# # Üç {'1': 'Bir', '2': 'İki', 1: 'Bir', '3': 'Üç'}
##### EKLEME
# sozluk = {"1":"Bir","2":"İki",1:"Bir"}
# sozluk["3"] = "Üç"
# print(sozluk) # {'1': 'Bir', '2': 'İki', 1: 'Bir', '3': 'Üç'}
#### GÜNCELLEME
# sozluk1 = {"1":"Bir","2":"İki","5":"Beş"}
# sozluk2 = {"1":"One","2":"Two","3":"Three","4":"Four"}
# sozluk1.update(sozluk2)
# print(sozluk1) 
# {'1': 'One', '2': 'Two', '5': 'Beş', '3': 'Three', '4': 'Four'}
#### Silme
# sozluk1 = {"1":"Bir","2":"İki","5":"Beş"}
# print(sozluk1.pop("1")) # Bir
# print(sozluk1) # {'2': 'İki', '5': 'Beş'}
###### item kavramı
# sozluk1 = {"1":"Bir","2":"İki","5":"Beş"}
# #           key:value
# #             item
# print(sozluk1.popitem()) # ('5', 'Beş')
# print(sozluk1) # {"1":"Bir","2":"İki"}
