
"""
import random as rnd
rnd.seed(0)
liste1 = [rnd.randint(1,50) for i in range(20)]
liste2 = [rnd.randint(1,50) for i in range(20)]
##################################################
yukarıdaki listelerden faydalanarak 
iki liste arasındaki farkı ve ortak sayıları bulan 
python kodunu yazınız

"""
import random as rnd
rnd.seed(0)
liste1 = [rnd.randint(1,50) for i in range(20)]
liste2 = [rnd.randint(1,50) for i in range(20)]


print(liste1.intersection(liste2))
print(liste1.difference(liste2))
