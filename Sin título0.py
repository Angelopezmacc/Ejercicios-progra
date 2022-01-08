import turtle
turtle.setup(700,700)
wn=turtle.Screen()
angel=turtle.Turtle()
a=int(input("ingrese el valor de lado: "))
b=a/2
c=b/2
d=c/2
e=d/2
f=e/2
g=f/2
h=g/2


def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
        
for i in [a,b,c,d,e,f,g,h]:
        angel.begin_fill()
        draw_poly(angel,4,i)
        angel.forward(i)
        angel.left(90)
        angel.forward(i)
        angel.right(90)
        angel.end_fill()
angel.penup()
angel.forward(50)
    

turtle.mainloop()
turtle.done()
turtle.bye()