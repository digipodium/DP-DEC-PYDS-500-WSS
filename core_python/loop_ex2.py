from turtle import *

speed('slowest')
side = 6
for i in range(side):
    forward(100)
    left(360//side)
    for i in range(5):
        forward(50)
        left(72)
        write(i)
mainloop() # keep the window open
