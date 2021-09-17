import turtle
turtle.speed(100)

def draw_squares(side):

    #square 1
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)

    #square 2
    turtle.forward(side/2)
    turtle.left(45)
    turtle.forward(side * (2 ** .5)/2)
    turtle.left(90)
    turtle.forward(side * (2 ** .5)/2) 
    turtle.left(90)
    turtle.forward(side * (2 ** .5)/2) 
    turtle.left(90)
    turtle.forward(side * (2 ** .5)/2) 
    turtle.left(90)

    #square 3
    (input('Press key to continue'))

draw_squares(100)

