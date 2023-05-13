# def topla(a,b):
#     return a+b

import os
import time
topla = lambda a,b:a+b
cikarma = lambda a,b:a-b
carpma = lambda a,b:a*b
bolme = lambda a,b:a/b
#         0       1      2      3
def main():
    try:
        liste = [topla,cikarma,carpma,bolme]
        islemListe = ["+","-","*","/"]
        islemAdi = ["Toplam","Çıkarma","Çarpma","Bölme"]
        menu = """
        1-Toplama
        2-Çıkarma 
        3-Çarpma  
        4-Bölme  
        5-Çıkış
        İşlem Seçimi Yapınız:
        """
        while True:
            print("#"*40)
            giris = input(menu)
            print("#"*40)
            if giris and giris.isdigit():
                giris = int(giris)
                if giris in (1,2,3,4):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{islemAdi[giris-1]} işlemi {islemListe[giris-1]}")
                    try:
                        a = int(input("1. Sayıyı Giriniz:"))
                        b = int(input("2. Sayıyı Giriniz:"))
                        sonuc = liste[giris-1](a,b)
                        print(f"{a} {islemListe[giris-1]} {b} = {sonuc}")
                    except ZeroDivisionError:
                        print("Sıfıra Sayı Bölmeye Çalıştın")
                    except ValueError:
                        print("Sayı yerine karakter girdin")
                    except Exception as hata:
                        print("Hata Verdi",hata)
                elif giris == 5:
                    break
                else:
                    print("Yanlış Giriş")
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as hata:
        print("Genel Hata",hata)


if __name__ == '__main__':
    main()
    
