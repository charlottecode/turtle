import turtle

turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,500)

side=6
angle=360/side

polygon=turtle.Turtle()
for i in range(side):
    polygon.forward(100)
    polygon.right(angle)
turtle.done()


