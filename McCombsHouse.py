import turtle
from turtle import *


def newTurtle():
    # Terry the turtle object
    terry = turtle.Turtle()
    print(terry.pos())
    # set his properties: shape, speed, colour...
    terry.shape('turtle')
    terry.speed(5)
    terry.pencolor("#575757")
    terry.fillcolor("#FCA756")
    # lift pen and reposition
    terry.up()
    terry.setpos(-100.00, -200.00)
    print(terry.pos())
    # start drawing McCombs house wall
    terry.begin_fill()
    terry.down()
    terry.fd(200)
    terry.left(90)
    terry.fd(250)
    terry.left(90)
    terry.fd(200)
    terry.left(90)
    terry.fd(250)
    terry.end_fill()

    # Martha the Turtle object for McCombs roof
    martha = turtle.Turtle()
    print(martha.pos())
    # set her properties: shape, speed, colour...
    martha.shape('turtle')
    martha.speed(2)
    martha.pencolor("#575757")
    martha.fillcolor("#841F27")
    # lift pen and reposition
    martha.up()
    martha.setpos(-120.00, 50.00)
    print(martha.pos())
    # start drawing McCombs roof
    martha.begin_fill()
    martha.down()
    martha.fd(240)
    martha.setpos(0.00, 200.00)
    martha.setpos(-120.00, 50.00)
    martha.end_fill()



    # TODO: McCombs Door - Laurence

    # Jake the Turtle object for McCombs roof
    jake = turtle.Turtle()
    print(jake.pos())
    # set her properties: shape, speed, colour...
    jake.shape('turtle')
    jake.speed(9)
    jake.pencolor("#575757")
    jake.fillcolor("Red")
    # lift pen and reposition
    jake.up()
    jake.setpos(-90.00, -200.00)
    print(jake.pos())
    # start drawing McCombs roof
    jake.begin_fill()
    jake.down()
    jake.fd(50)
    jake.left(90)
    jake.fd(85)
    jake.left(90)
    jake.fd(50)
    jake.left(90)
    jake.fd(85)
    jake.end_fill()
    # door frame

    jake.left(90)
    jake.fd(5)
    jake.left(90)
    jake.fd(80)
    jake.right(90)
    jake.fd(40)
    jake.right(90)
    jake.fd(80)
    # handle
    jake.up()
    jake.setpos(-55.00, -160.00)
    jake.down()

    # TODO: McCombs Windows & Decorations - Liam
    # TODO: Git merger

    # end
    turtle.exitonclick()


newTurtle()
