class Musteri:
    def __init__(self,adi,soyadi,telefon):
        self.adi = adi
        self.soyadi = soyadi
        self.telefon = telefon
        self._id = None

    
    def musteriBilgi(self):
        return self.adi,self.soyadi,self.telefon
    
    def musteriEkleDB(self,objDB):
        try:
            sorgu = f"""
            INSERT INTO musteri_bilgi
            (musteri_adi,musteri_soyadi,musteri_telefon)
            VALUES ('{self.adi}','{self.soyadi}',{self.telefon})"""
            if objDB.sorguIDU(sorgu):
                return "Başarıyla Eklendi"
        except Exception as hata:
            return str(hata)


    @classmethod
    def musteriListele(cls,objDB):
        sorgu = """
        SELECT musteri_id, 
        musteri_adi, 
        musteri_soyadi, 
        musteri_telefon
        FROM musteri_bilgi;
        """
        return objDB.sorguSelect(sorgu)

    def musteriSil(self,objDB):
        sorgu = f"""
        DELETE FROM musteri_bilgi WHERE musteri_id = {self._id}
        """
        return objDB.sorguIDU(sorgu)

    def bilgiGuncelle(self,objDB):
        try:
            sorgu = f"""
            UPDATE musteri_bilgi SET 
            musteri_adi = '{self.adi}',
                musteri_soyadi = '{self.soyadi}',
                musteri_telefon = {self.telefon} 
                WHERE musteri_id = {self._id};
            """
            if objDB.sorguIDU(sorgu):
                return "Başarıyla Güncellendi"
        except Exception as hata:
            return str(hata)

    def musteriBilgiSelect(self,objDB):
        try:
            sorgu = f"""
            SELECT musteri_id
            FROM musteri_bilgi
            WHERE  musteri_adi = '{self.adi}' AND 
            musteri_soyadi = '{self.soyadi}' AND 
            musteri_telefon = {self.telefon};
            """
            self._id = objDB.sorguSelect(sorgu)[0][0]
            return self._id
        except:
            return -1
