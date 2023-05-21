import sqlite3 as sql
db = sql.connect("DB\chinook.db")
cur = db.cursor()
sart = input("Müşteri Id Giriniz:")
sorgu = f"""
SELECT 
FirstName,LastName,City
FROM customers WHERE CustomerId = {sart}
"""
# print(*cur.execute(sorgu).fetchall(),sep="\n")
sonuclar = cur.execute(sorgu).fetchall()
for a,b,c in sonuclar:
    print(a,b,c)
