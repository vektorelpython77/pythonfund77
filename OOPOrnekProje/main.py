from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QListWidgetItem
from PyQt5.uic import loadUi
import sys
from PYS.db import DBTool
from PYS.core import Musteri
class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.adres = r"OOPOrnekProje\DB\\"
        self.db = DBTool(self.adres)
        self.musteri = None
        self.initUI()

    def initUI(self):
        loadUi(r"OOPOrnekProje\UI\anamenu.ui",self)
        self.btEkle.clicked.connect(self.musteriYeni)
        self.btSil.clicked.connect(self.musteriSil)
        self.btKaydet.clicked.connect(self.musteriKaydet)
        self.lstMusteri.clicked.connect(self.secilenMusteri)
        self.show()
        self.musteriListele()

    def mesajYaz(self,mesaj,tip):
        if tip == 1:
            QMessageBox.information(self,"Bilgi",mesaj)
        elif tip == 2:
            QMessageBox.warning(self,"Bilgi",mesaj)

    def musteriYeni(self):
        self.temizle()
        self.musteri = None


    def musteriKaydet(self):
        if not self.musteri:
            ad = self.txtAd.text()
            soyad = self.txtSoyad.text()
            telefon = self.txtTel.text()
            self.musteri = Musteri(ad,soyad,telefon)
            mesaj = self.musteri.musteriEkleDB(self.db)
            if mesaj != "Başarıyla Eklendi":
                self.mesajYaz(mesaj,2)
            else:
                self.mesajYaz(mesaj,1)
        else:
            self.musteri.adi = self.txtAd.text()
            self.musteri.soyadi = self.txtSoyad.text()
            self.musteri.telefon = self.txtTel.text()
            mesaj = self.musteri.bilgiGuncelle(self.db)
            if mesaj != "Başarıyla Güncellendi":
                    self.mesajYaz(mesaj,2)
            else:
                self.mesajYaz(mesaj,1)
                self.temizle()
                self.lstMusteri.clear()
                self.musteriListele()
        
    def musteriListele(self):
        liste = Musteri.musteriListele(self.db)
        for item in liste:
            bilgi = list(map(str,item))
            self.lstMusteri.addItem(" ".join(bilgi[1:]))

    def secilenMusteri(self):
        try:
            ad,soyad,tel = QListWidgetItem(self.lstMusteri.currentItem()).text().split()
            self.musteri = Musteri(ad,soyad,tel)
            _id = self.musteri.musteriBilgiSelect(self.db)
            if _id > 0:
                self.txtAd.setText(ad)
                self.txtSoyad.setText(soyad)
                self.txtTel.setText(tel)
                self.musteri._id = _id
            else:
                self.temizle()
        except:
            pass
    
    def musteriSil(self):
        if self.musteri._id:
            self.musteri.musteriSil(self.db)
            self.lstMusteri.clear()
            self.temizle()
            self.musteriListele()
        else:
            self.mesajYaz("Silinecek Kayıt Yok",2)

    def temizle(self):
        self.txtAd.setText("")
        self.txtSoyad.setText("")
        self.txtTel.setText("")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = App()
    sys.exit(app.exec_())