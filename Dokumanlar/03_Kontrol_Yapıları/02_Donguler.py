"""
1. range
2. for 
3. while
4. break,else,continue
"""
##### range
print(*range(0,6)) # 0 1 2 3 4 5
print(*range(6)) # 0 1 2 3 4 5
print(*range(6,0,-1)) # 6 5 4 3 2 1
print(*range(5,30,5)) # 5 10 15 20 25
###################### for
for i in range(6):
    print(i*"* ")
var1 = "Vektorel"
#       01234567
# var1[0] => V
########
# for i in range(len(var1)): # 0 1 2 3 4 5 6 7
#     print(var1[i])
#########
# for ch in var1: # V e k t o r e l
#     print(ch)
var1 = """
Rapor: Hindistan, 2026 yılına kadar dünyanın 
en büyük ikinci güneş fotovoltaik üreticisi olabilir
"""
# for item in var1:
#     if item.isupper():
#         print(item)

print(set([item for item in var1 if item.islower()]))
import collections as col
print(col.Counter(var1))