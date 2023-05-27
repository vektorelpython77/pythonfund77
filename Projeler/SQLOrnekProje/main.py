import sqlite3 as sql
import os
print(os.path.dirname(__file__))
def dbinit():
    dbName = "musteriler.db"
    adres = os.path.dirname(__file__) + os.sep + dbName
    db = sql.connect(adres)
    cur = db.cursor()
    tabloScript = """
    CREATE TABLE IF NOT EXISTS musteri_bilgi (
        musteri_id     INTEGER  PRIMARY KEY AUTOINCREMENT,
        musteri_adi    TEXT     NOT NULL,
        musteri_soyadi TEXT     NOT NULL,
        musteri_email  TEXT     NOT NULL,
        kayit_zaman    DATETIME DEFAULT (datetime() ) 
                                NOT NULL
    );
    """
    cur.execute(tabloScript)
    tabloScript = """
    CREATE UNIQUE INDEX IF NOT EXISTS UIDX_MUSTERI_ADI_SOYADI ON musteri_bilgi (
        musteri_adi,
        musteri_soyadi
    );

    """
    cur.execute(tabloScript)    
    db.commit()
    return cur,db

def veriSil(id):
    cur,db = dbinit()
    try:
        sorgu = f"""
        DELETE FROM musteri_bilgi WHERE
        musteri_id = {id}
        """
        cur,db = dbinit()
        cur.execute(sorgu)
        db.commit()
        return True
    except sql.Error as hata:
        print(hata)
        db.rollback()
        return False
    finally:
        db.close()

def veriEkle(isim,soyisim,email):
    cur,db = dbinit()
    try:
        sorgu = f"""
        INSERT INTO musteri_bilgi (
        musteri_adi,musteri_soyadi,musteri_email
        ) VALUES ('{isim}','{soyisim}','{email}')
        """
        cur,db = dbinit()
        cur.execute(sorgu)
        db.commit()
        return cur.lastrowid
    except sql.Error as hata:
        print(hata)
        db.rollback()
    finally:
        db.close()



def veriGuncelle(id,**kwargs):
    liste = []
    for key,value in kwargs.items():
        if key == "adi":
            liste.append(f"musteri_adi='{value}'")
        if key == "soyadi":
            liste.append(f"musteri_soyadi='{value}'")
        if key == "email":
            liste.append(f"musteri_email='{value}'")
    updatemetin = ",".join(liste)
    sorgu = f"""
    update musteri_bilgi set {updatemetin} 
    where musteri_id = {id}
    """
    cur,db = dbinit()
    cur.execute(sorgu)
    db.commit()

veriGuncelle(537,adi="Ahmet Bera",soyadi="Demir",email="aaa@aaa.com")



# print(veriEkle('Vektorel1','Bilişim','vektorelpython77@gmail.com'))



# import time
# def zaman(fonk):
#     def innerFonk(*args,**kwargs):
#         baslangic  = time.time()
#         fonk(*args,**kwargs)
#         bitis = time.time()
#         print(f"""
#         {fonk.__name__} isimli fonksiyon için 
#         geçen süre {bitis-baslangic}
#         """)
#     return innerFonk

# def topluAktar(adresDosya):

# dosyaAdres = os.path.dirname(__file__) + os.sep + "ornek.csv"

# def topluVeriEkle(adres):
#     with open(adres) as dosya:
#         i = 0
#         liste = dosya.readlines()
#         for i in range(1,len(liste)):
#             _,adi,soyadi,email,_ = liste[i].split(",")
#             veriEkle(adi,soyadi,email)


# def scriptileTopluVeriEkle(adres):
#     sorgu = """
#      INSERT INTO musteri_bilgi (
#         musteri_adi,musteri_soyadi,musteri_email
#         ) VALUES 

#     """
#     with open(adres) as dosya:
#         i = 0
#         liste = dosya.readlines()
#         for i in range(1,len(liste)):
#             _,adi,soyadi,email,_ = liste[i].split(",")
#             sorgu += f"('{adi}','{soyadi}','{email}'),"
#         else:
#             sorgu = sorgu[:-1]
#             sorgu += ";"
#     cur,db = dbinit()
#     cur.execute(sorgu)
#     db.commit()


# # topluVeriEkle(dosyaAdres)

# scriptileTopluVeriEkle(dosyaAdres)