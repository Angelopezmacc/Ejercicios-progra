import turtle
import math
turtle.setup(700,700)
wn=turtle.Screen()
angel=turtle.Turtle()

def figura_5(angel,x):
    a=x/3
    b=a**2+a**2
    for i in range(4):
         angel.forward(x)
         angel.left(135)
         angel.forward(math.sqrt(b))
         angel.left(135)
         
figura_5(angel,300)         
        

turtle.mainloop()
turtle.done()
turtle.bye()
