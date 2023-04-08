#### Tanımlama
var1 = ()
print(type(var1)) # <class 'tuple'>
var1 = (1)
print(type(var1)) # <class 'int'>
var1 = (1,)
print(type(var1)) # <class 'tuple'>
var1 = 1,2,3
print(type(var1)) # <class 'tuple'>
############ Erişimde List ve str veri tiplerinden farkı yoktur
var1 = 1,2,3
print(var1[0])
########### count,index
var1.index(1)
var1.count(1)
