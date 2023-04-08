
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
x=set(liste1)
y=set(liste2)
print(x.difference(y))
print(x.intersection(y))
print(x.symmetric_difference(y))