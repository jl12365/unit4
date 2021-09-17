import turtle
import pixelart

def test_initialize():
    pixelart.initialize()
    assert turtle.xcor() == -300
    assert turtle.ycor() == 300
    assert turtle.speed(10)
    assert turtle.penup()
    assert turtle.pensize() == 1
    assert turtle.fillcolor() == 'white'
    assert turtle.pencolor() == 'black'
    assert turtle.setheading(0)