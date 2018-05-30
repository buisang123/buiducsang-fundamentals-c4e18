
from turtle import *
color1 = ('red','blue','brown','yellow','grey')
k = 0
for i in range(3,8):
    color(color1[k])
    for j in range(i):
        forward(100)
        left(360 / i )
       
    k += 1

            
mainloop()
