import PIL
import turtle as trtl
turtle = trtl.Turtle()
turtle.speed(100)
colors = ["black", "white"]
circle_size = 1
color_count = 0
turtle.shape("circle")
while True:
    circle_size = 1
    while circle_size < 25:
        turtle.color("purple")
        turtle.shapesize(circle_size)
        turtle.stamp()
        circle_size += 1
    circle_size = 1
    while circle_size < 25:
        turtle.color("blue")
        turtle.shapesize(circle_size)
        turtle.stamp()
        circle_size += 1
    circle_size = 1
    while circle_size < 25:
        turtle.color("pink")
        turtle.shapesize(circle_size)
        turtle.stamp()
        circle_size += 1
wn = trtl.Screen()
wn.mainloop()