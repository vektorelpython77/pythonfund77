
"""
https://codeshare.io/MNLMDy

Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
# 0  2  4  6     8                                   1  3  5     7
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
Kurallar http://www.kodaman.org/yazi/t-c-kimlik-no-algoritmasi adresinden alınmıştır.
"""
tcno = "10000000146"
# tcno = input("TC Kimlik Numaranızı Giriniz:")
tcno = input("TC Kimlik Numaranızı Giriniz:")
if len(tcno) == 11:
    if tcno.isdigit():
        if tcno[0] != "0" and tcno[-1] != "0":
            toplam1 = sum([int(tcno[i]) for i in range(0,9,2)]) # 0 2 4 6 8
            toplam2 = sum([int(tcno[i]) for i in range(1,8,2)]) # 1 3 5 7
            if (toplam1*7-toplam2)%10 == int(tcno[9]):
                # toplam3 = 0
                # for i in range(0,10): # 0 1 2 3 4 5 6 7 8 9
                #     toplam3 += int(tcno[i])
                if sum([int(tcno[i]) for i in range(0,10)])%10 == int(tcno[10]):
                    print("Doğru")
                else:
                    print("Kural 5")
            else:
                print("Kural 4")
        else:
            print("Kural 3")
    else:
        print("Kural 2")
else:
    print("Kural 1")

