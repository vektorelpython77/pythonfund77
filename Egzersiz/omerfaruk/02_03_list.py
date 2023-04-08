
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
# soru 1
#liste = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#del liste[0]
#del liste[4]
#liste.pop()
#print(liste)

#soru 2 (1)
# liste1 = [25,41,52,63,85,74]
# liste2 = [3969,5476]
# liste3 = liste1+liste2
# print(liste3)

#soru 2 (2)
#liste = [25,41,52,63,85,74]
#liste[2] = 2704 
#liste[4] = 7225
#print(liste)

 #soru 2 (3)
# liste = [25,41,52,63,85,74]
# del liste[0]
# print(liste)

#soru 2 (4)
# liste1 = [25,41,52,63,85,74]
# liste2 = [456,789,234]
# liste1.extend(liste2)
# print(liste1)

# #soru 3 (1)
# liste = [12,2,2,2,3,3,3,1,1,1,2,2]
# print(len(liste))

#soru 3 (2)
# liste = [12,2,2,2,3,3,3,1,1,1,2,2]
# print(" listedeki en büyük sayıyı yazdırınız: ", max(liste))

#soru 3 (3)
# liste = [12,2,2,2,3,3,3,1,1,1,2,2]
# print(" listedeki en büyük sayıyı yazdırınız: ", min(liste))

#soru 3 (4)
liste = [12,2,2,2,3,3,3,1,1,1,2,2]
print(" listedeki sayıların toplamını yazdırınız ", sum(liste))














