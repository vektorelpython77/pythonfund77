# isim =input("isminizi giriniz: ")
# print("merhaba", isim)
sozluk = {"1":"Bir","2":"İki",3:"beş"}
print(sozluk["1"])
print(sozluk[3])


sayi = input("6 basamaklı bir sayı giriniz: ")
#if sayi and isdigit():

birlerbsm    = sayi%10
onlarbsm     = (sayi%100)//10
yüzlerbsm    = (sayi%1000)//100
binlerbsm    = (sayi%10000)//1000
onbinlerbsm  = (sayi%100000)//10000
yüzbinlerbsm = (sayi%1000000)//100000


