try:
    adim = "1AE1"
    a = int(input("1. Sayıyı Giriniz:"))
    adim = "1AE2" 
    b = int(input("2. Sayıyı Giriniz:"))
    adim = "1AE3"
    print(a/b)
except ZeroDivisionError:
    print("Sıfıra Sayı Bölmeye Çalıştın",adim)
except ValueError:
    print("Sayı yerine karakter girdin",adim)
except Exception as hata:
    print("Hata Verdi",hata,adim)
finally:
    print("Finally çalıştı")