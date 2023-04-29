
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

def  isValidTCID(value):
    value = str(10000000146)
    
    if not len(value) == 11:
        return False
    

    if not value.isdigit():
        return False
    

    if int(value[0]) == 0:
        return False
    
    digits = [int(d) for d in str(value)]
    

    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    

    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    
    
    
 