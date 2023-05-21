import sqlite3 as sql
db = sql.connect("DB\chinook.db")
cur = db.cursor()
try:
    sorgu1 = """
    INSERT INTO Customers (FirstName,LastName,Email) VALUES
    ('Vektorel','Bilisim','aa@aa.com')
    """
    cur.execute(sorgu1)
    db.commit()
except sql.DatabaseError as hata:
    print(hata)
    db.rollback()



# sart = input("Müşteri Id Giriniz:")
sorgu = f"""
SELECT 
CustomerId,FirstName,LastName
FROM customers  ORDER BY CustomerId DESC LIMIT 1
"""
# print(*cur.execute(sorgu).fetchall(),sep="\n")
sonuclar = cur.execute(sorgu).fetchall()
for a,b,c in sonuclar:
    print(a,b,c)