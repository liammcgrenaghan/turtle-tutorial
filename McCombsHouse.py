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
    print(terry.pos())
    # start drawing McCombs roof
    martha.begin_fill()
    martha.down()
    martha.fd(240)
    martha.setpos(0.00, 200.00)
    martha.setpos(-120.00, 50.00)
    martha.end_fill()

    #TODO: Mccombs Windows & Decorations - Liam
    #TODO: Mccombs Door - Laurence
    #TODO: Git merger

    # end
    turtle.exitonclick()


newTurtle()
