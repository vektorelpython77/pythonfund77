import sqlite3 as sql

class DBTool:
    def __init__(self,adres):
        dbName = "musteriler.db"
        adres = adres + dbName
        self.db = sql.connect(adres)
        self.cur = self.db.cursor()
        tabloScript = """
        CREATE TABLE IF NOT EXISTS musteri_bilgi (
            musteri_id     INTEGER  PRIMARY KEY AUTOINCREMENT,
            musteri_adi    TEXT     NOT NULL,
            musteri_soyadi TEXT     NOT NULL,
            musteri_telefon  INTEGER  NOT NULL,
            kayit_zaman    DATETIME DEFAULT (datetime() ) 
                                    NOT NULL
        );
        """
        self.cur.execute(tabloScript) 
        self.db.commit()

    def sorguSelect(self,sorgu):
        self.cur.execute(sorgu)
        return self.cur.fetchall()
    
    def sorguIDU(self,sorgu):
        try:
            self.cur.execute(sorgu)
            self.db.commit()
            return True
        except sql.Error as hata:
            self.db.rollback()
            raise Exception(hata)
        
    
