
"""
1. Sıfırdan dokuza kadar olan rakamları ve okunuşlarını 
bir sözlük içerisine yazınız
2. üç rakamdan oluşan bir str veri tipinde sayının, sıfırıncı indisinde bulunan
rakamın okunuşunu ekrana yazdırabilmek için 1. adımda oluşturduğunuz sözlüğü kullanınız.
"""



sozluk ={"1": "bir","2": "iki","3": "üc","4": "dort","5": "bes","6":"altı","7": "yedi","8": "sekiz","9: dokuz"}
sayı ="123"
print(sozluk.get(sayı[0]))