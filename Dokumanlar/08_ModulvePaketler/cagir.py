# from paket import Paket
# Paket()
# from paket.paket2 import Paket2
# Paket2()
##############################
# import os
# os.path
##############################
# from os import path,environ
# path.join
# environ.update
##############################
import pymongo
def baglan():
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    uri = "mongodb+srv://vektorelpython77:vektorelpythonnosql@vektorel.8gwojco.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        return client
    except Exception as e:
        raise Exception(e)
    
# istemci = baglan()
# mydb = istemci["ibrahim"]
# print(istemci.list_database_names())
# if "ibrahim"  in istemci.list_database_names():
#     print("Veritabanı zaten var")
# mycol = mydb["vektorel"]

# mydb = istemci["sample_analytics"]
# print(mydb.list_collection_names())


######################
def veriEkle(isim,soyisim,adres):
    istemci = baglan()
    db = istemci["ibrahim"]
    kol = db["vektorel"]
    sozluk = {"isim":isim,"soyisim":soyisim,"adres":adres}
    sonuc = kol.insert_one(sozluk)
    return sonuc.inserted_id
print(veriEkle("Süleyman","Demir","Ankara")) # 64858950d9c21b24cb7fba32