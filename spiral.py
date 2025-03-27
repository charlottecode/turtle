import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(500,500)

mypen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        mypen.forward(size+1)
        mypen.left(90)
        size=size-5
    size=size+1
turtle.done()

