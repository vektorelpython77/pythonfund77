"""
recursion
özyineleme
"""
def fonk(metin):
    print(metin)
fonk("BEŞİKTAŞ")

"""
Beşiktaş
Beşikta
Beşikt
Beşik
Beşi
Beş
Be
B
"""
def fonk(metin):
    if len(metin) == 1:
        print(metin)
    else:
        print(metin)
        fonk(metin[:-1])

def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)
print(faktoriyel(5))

