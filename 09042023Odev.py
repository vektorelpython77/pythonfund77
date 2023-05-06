"""
1. Aşağıdaki şekli ekrana yazdıran python kodunu yazınız
#
# # 
# # # 
# # # # 
# # # # # 
# # # # # #
# # # # # 
# # # # 
# # # 
# # 
#
"""

"""
2. 
1 ile 150 sayıları arasındaki sayılardan 15'e tam bölünebilen 
sayıların listesini ekrana yazdıran python kodunu yazınız
"""

"""
3.
fibanocci serisinde verilen sınıra kadar seri elemanlarını ekrana 
yazdıran programı yazınız
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()