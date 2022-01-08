import turtle

peter=turtle.Turtle()

largo=int(input("Ingrese el largo del triángulo: "))

for i in range(3):
    turtle.forward(largo)
    turtle.left(120)

turtle.forward(largo/2)
turtle.right(90)
turtle.penup()
turtle.forward(largo/4)
turtle.left(150)
turtle.pendown()

for i in range(3):
    turtle.forward(largo)
    turtle.left(120)  
 
turtle.shape("turtle")

peter=turtle.Turtle
   

turtle.exitonclick()