def bolme(a,b):
    if a == 0 or b == 0:
        raise Exception("Sıfır Hatası")
    else:
        return a/b


try:
    adim = "1AE1"
    a = int(input("1. Sayıyı Giriniz:"))
    adim = "1AE2" 
    b = int(input("2. Sayıyı Giriniz:"))
    adim = "1AE3"
    # assert b != 0, "Sıfır Hatası 22222222222222222"
    print(bolme(a,b))
except AssertionError as hata:
    print(hata)
except ZeroDivisionError:
    print("Sıfıra Sayı Bölmeye Çalıştın",adim)
except ValueError:
    print("Sayı yerine karakter girdin",adim)
except Exception as hata:
    print("Hata Verdi",hata,adim)


##########################
# x = "Selam"
# assert x != "Selam", "x Hoşçakal Olmalıydı"