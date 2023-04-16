
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
# 1. soru:
liste=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
x=print(liste[1:4])
print(x.pop(0))


#2.soru

liste2 = [25,41,52,63,85,74]
(liste2[3])
(liste2[5])

(liste2.append(3969))

(liste2.append(5476))
print(liste2)

liste2[2]=2704
liste2[4]=7225
print(liste2)

(liste2.remove(25))
print(liste2)

# 3
ph= [12,2,2,2,3,3,3,1,1,1,2,2]
print(len(ph))

print(max(ph))
print(min(ph))
print(sum(ph))


print("/".join(ph))