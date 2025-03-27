import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(400,400)

side=5
angle=144

star=turtle.Turtle()
for i in range(side):
    star.forward(100)
    star.right(angle)
turtle.done()