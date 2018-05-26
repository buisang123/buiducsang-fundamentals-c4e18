from turtle import *
speed(-1)
shape("turtle")
color("green")
fillcolor("green")
begin_fill()
for i in range(6):
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    left(60)
forward(100)
end_fill()

mainloop()
