import turtle
turtle.setup(400,300)
wn=turtle.Screen()
angel=turtle.Turtle()
#forma1
"""
for i in range(4):
    angel.forward(100)
    angel.left(90)
    angel.forward(50)
    angel.right(90)
    angel.forward(50)
    angel.left(90)
"""    
#forma2
""""

angel.forward(100)
angel.left(90)
angel.forward(50)
angel.right(90)
angel.forward(50)
angel.left(90)
angel.forward(100)
angel.left(90)
angel.forward(50)
angel.right(90)
angel.forward(50)
angel.left(90)
angel.forward(100)
angel.left(90)
angel.forward(50)
angel.right(90)
angel.forward(50)
angel.left(90)
angel.forward(100)
angel.left(90)
angel.forward(50)
angel.right(90)
angel.forward(50)

"""
#forma3
def figura_1 (angel,x):
    for i in range(4):
        angel.forward(x)
        angel.left(90)
        angel.forward(x/2)
        angel.right(90)
        angel.forward(x/2)
        angel.left(90)
        
figura_1(angel,200)

turtle.mainloop()
turtle.done()
turtle.bye()




