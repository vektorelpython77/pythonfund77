
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

liste = ['red','green','white','black','pink','yellow']
#         0       1       2       3       4       5
del  liste[0]
print(liste)
del  liste[4]
print(liste)
del  liste[3]
print(liste)




liste = [25,41,52,63,85,74]
#         0  1  2  3  4  5
liste.append(3969)
liste.append(5476)
print(liste)

liste[2] = 2704
liste[4] = 7225
print(liste)

del  liste[1]
print(liste)

liste2 = [456,789,234]
liste.extend(liste2)
print(liste)


liste = [12,2,2,2,3,3,3,1,1,1,2,2]
print(len(liste))
print(max(liste))
print(min(liste))
print(sum(liste))




