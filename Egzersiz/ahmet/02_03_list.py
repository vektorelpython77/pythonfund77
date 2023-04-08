
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
liste = ["Red","Green","white","Black","Pink","Yellow"]
del liste[0]
del liste[3]
del liste[3]
print(liste)

liste1 = [25,41,52,63,85,74] #yukarıdaki listede yer alan 3. ve 5. elemanların karesini liste sonuna ekleyiniz
liste1.append(52*52)
liste1.append(85*85)
print(liste1)
liste1[1]=41*41
liste1[3]=63*63
print(liste1)
del liste1[0]
print(liste1)
liste2=[456,789,234]
liste1.extend(liste2)
print(liste1)
liste3 = [12,2,2,2,3,3,3,1,1,1,2,2]
print(len(liste3))
print(max(liste3))