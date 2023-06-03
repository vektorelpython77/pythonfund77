
"""
1. Para Çekme
2. Para Yatırma
3. Havale
4. Bakiye Görüntüleme
5. Hesap Aç/Kapat
5. Çıkış
"""

# https://codeshare.io/gLlKK8
####################################################################
hesapListe = [] # global değişken
adres = r"Projeler\Dosyalamaİslemleri\banka.csv"

def dosyaAcKapat(adres,mod,veri=[]):
    try:
        if not veri: # verinin boş gelmesi durumunda
            dosya = open(adres,mod,encoding="UTF-8")
            dosya.seek(0)
            liste =  dosya.readlines() # dosya içindeki tüm satırlar okunuyor
            return liste # tüm bilgi dışarı aktarılıyor
        else: # verinin dolu olması durumunda 
            dosya = open(adres,mod,encoding="UTF-8")
            dosya.seek(0)
            dosya.truncate() # dosya içeriği temizleniyor
            dosya.writelines(veri) # dosyaya bilgi yazılıyor
            dosya.close()
            return [1]
    except Exception as hata: 
        print("Hata",hata)

def islemarac(hesapId,**kwargs):
    for key,value in kwargs.items():
        if key == "havale": # parametre havale ise değerin [200,2,3] => [tutar,gelen hesap,"giden hesap"]
            if cekYatir(value[1],value[0],1): # para gelen hesaptan çekilecek
                cekYatir(value[2],value[0],2) # giden hesaba eklenecek
                
        if key == "yatir": # parametre yatir ise değerin [200]
            cekYatir(hesapId,value[0],2)
        if key == "cek":
            cekYatir(hesapId,value[0],1)
        if key == "ackapat": # parametre ackapat ise ["1","Ali Veli","USD","200"] 
            """
            ["1","Ali Veli","USD","200"]  => ["Açma Kapatma","Hesap Bilgisi";"Tip","Tutar"]
            """
            if hesapId == "0":
                if value[0] == 1: # Hesap Açmak 
                    value = value[1:]
                    value[-1] += "\n"
                    hesapListe.append(";".join(value))
                elif value[0] == 2: # hesap Kapalı
                    value = value[1:]
                    for i in range(len(hesapListe)):
                        satir = hesapListe[i]
                        if satir[1:] == value:
                            hesapListe.pop(i)



def gitGetir(hesapId):
    for i in range(len(hesapListe)):
        if hesapListe[i].split(";")[0] == hesapId:
            return i
    else:
        raise Exception("Hesap Bulunamadı")

def cekYatir(hesapId,tutar,cekYatir):
    try:
        tutar = int(tutar)
        satir =  hesapListe[gitGetir(hesapId)].split(";") # 1;Ali Veli;USD;1200\n => ["1","Ali Veli","USD","1200\n"]
        hesapid,adi,tur,para = satir # "1","Ali Veli","USD","1200\n"
        # para = para[:-2]  # "1200\n" => "1200"
        if cekYatir == 1: # para çekme
            if int(para) < tutar: # hesapta para yoksa 
                raise Exception("Yetersiz Bakiye")
            para = str(int(para) - tutar) + "\n" # => str(1200-200) + "\n" => "1000\n"
        if cekYatir == 2: # para yatırma
            para = str(int(para) + tutar) + "\n"
        satir[3] = para # para güncelleniyor
        hesapListe[gitGetir(hesapId)] = ";".join(satir) # liste güncelleniyor
        return True  # işler yolunda gittiyse dışarı yapıldı bilgisi gidiyor
    except Exception as hata:
        print("Hata cekyatir",hata)
        return False # sorun var demektir log yazılabilir

def hesaplisteleme():
    for item in hesapListe:
        print(*item.split(";"),sep="-",end="")


def paracekme():
    hesaplisteleme()
    hesapId = input("İşlem Yapmak istediğiniz hesap numarasını giriniz:")
    tutar = input("Çekmek istediğiniz tutarı giriniz")
    islemarac(hesapId,cek=[tutar])

def parayatirma():
    hesaplisteleme()
    hesapId = input("İşlem Yapmak istediğiniz hesap numarasını giriniz:")
    tutar = input("Yatırmak istediğiniz tutarı giriniz")
    islemarac(hesapId,yatir=[tutar])

def havale():
    hesaplisteleme()
    hesapId1 = input("Parayı çekmek istediğiniz hesap numarasını giriniz:")
    hesaplisteleme()
    hesapId2 = input("Parayı Yatırmak istediğiniz hesap numarasını giriniz:")
    tutar = input("Yatırmak istediğiniz tutarı giriniz")
    islemarac(hesapId1,havale=[tutar,hesapId1,hesapId2])
    hesaplisteleme()

def hesapAcmaKapatma():
    islem = input("""
1.Hesap Açma
2.Hesap Kapatma
İşlem Seçiniz:""")
    if islem == "1":
        islemarac("0",)


def main():
    menu = """
1. Para Çekme
2. Para Yatırma
3. Havale
4. Bakiye Görüntüleme
5. Hesap Aç/Kapat
6. Çıkış
""" + "#"*51 + """
İşlem Seçiniz:"""
    print("#"*20,"Hoşgeldiniz","#"*20)
    global hesapListe
    hesapListe = dosyaAcKapat(adres,"r+") # dosyadaki hesap bilgileri okundu
    islem = input(menu)
    if islem == "1":
        paracekme()
    if islem == "2":
        parayatirma()
    if islem == "3":
        havale()
    # hesaplisteleme()
    dosyaAcKapat(adres,"r+",hesapListe)
    
main()


