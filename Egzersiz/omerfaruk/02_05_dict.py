
"""
1. Sıfırdan dokuza kadar olan rakamları ve okunuşlarını 
bir sözlük içerisine yazınız
2. üç rakamdan oluşan bir str veri tipinde sayının, sıfırıncı indisinde bulunan
rakamın okunuşunu ekrana yazdırabilmek için 1. adımda oluşturduğunuz sözlüğü kullanınız.
"""


a = {"0":"sıfır,"1":"Bir", "2":"İki", "3":"Üç", "4":"Dört", "5":"Beş", "6":"Altı", "7":"Yedi", "8":"Sekiz", "9":"Dokuz"}
sayi = "123"

print(sozluk[sayi[0]])
print(sozluk.get(sayi[0]))
