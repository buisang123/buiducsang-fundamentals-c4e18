from turtle import *
for i in range(3,7):
    if i % 2 != 0:
        for j in range(i):
            color("green")
            forward(100)
            left(360 / i )
    else:
        for j in range(i):
            color("red")
            forward(100)
            left(360 / i)

mainloop()
