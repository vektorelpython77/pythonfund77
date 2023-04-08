
"""
1. Sıfırdan dokuza kadar olan rakamları ve okunuşlarını 
bir sözlük içerisine yazınız
2. üç rakamdan oluşan bir str veri tipinde sayının, sıfırıncı indisinde bulunan
rakamın okunuşunu ekrana yazdırabilmek için 1. adımda oluşturduğunuz sözlüğü kullanınız.
"""
sozluk ={"0":"Sıfır",
"1":"bİR",
"2":"iki",
"3":"üç",
"4":"dört",
"5":"beş","6":"altı","7":"yedi","8":"sekiz","9":"dokuz"}
sayi = "123"
print(sozluk[sayi[0]])
print(sozluk.get(sayi[0]))
