from turtle import*
color2 = ('red','blue','brown','yellow','grey')
k = 0

for i in range(5):
    color(color2[k])
    fillcolor(color2[k])
    begin_fill()
    
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(100)
    k += 1
    end_fill()





mainloop()

