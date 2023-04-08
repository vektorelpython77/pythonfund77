
"""
Egzersiz_1
1. Soru
liste = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Beklenen => ['Green', 'White', 'Black']

yukarıdaki listenin 0,4 ve 5. elemanlarını siliniz
2. Soru
liste = [25,41,52,63,85,74]
    - yukarıdaki listede yer alan 3. ve 5. elemanların karesini liste sonuna ekleyiniz
    - 2. ve 4. elemanın karesini kendi yerinde güncelleyiniz
    - 1. elemanı siliniz
    - [456,789,234] sayılarını liste içerisine genişleterek ekleyiniz
3.
liste = [12,2,2,2,3,3,3,1,1,1,2,2]
    a. yukarıdaki listenin uzunluğunu ekrana yazdırınız
    b. listedeki en büyük sayıyı yazdırınız (araştırma)
    c. listedeki en küçük sayıyı yazdırınız (araştırma)
    d. listedeki sayıların toplamını yazdırınız (araştırma)

"""
liste = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
liste.pop(0)
liste.pop(4)
liste.pop(5)
print(liste)

liste = [25,41,52,63,85,74]
liste.append([-1],**2)
liste.append([-3],**2)
print(liste)

liste[1]=liste[1]**2
liste[3]=liste[3]**2
prin

liste = [12,2,2,2,3,3,3,1,1,1,2,2]
eleman_sayısı=len(liste)
print(eleman_sayısı)


liste = [12,2,2,2,3,3,3,1,1,1,2,2]
en_kucuk = min(liste)
en_buyuk = max(liste)
print("Liste İçindeki En Büyük Sayı :", en_buyuk, "\nListe İçindeki En Büyük Sayı :",en_kucuk)

liste = [12,2,2,2,3,3,3,1,1,1,2,2]
toplam = sum(liste)
print(toplam)