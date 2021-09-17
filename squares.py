import turtle
turtle.speed(100)

def draw_squares(side):

    #square 1
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.end_fill()

    #square 2
    turtle.begin_fill()
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
    turtle.fillcolor('blue')
    turtle.end_fill()

    #square 3
    turtle.begin_fill()
    turtle.forward(side* (2 ** .5)/4)
    turtle.left(45)
    turtle.forward(side/2)
    turtle.left(90)
    turtle.forward(side/2)
    turtle.left(90)
    turtle.forward(side/2)
    turtle.left(90)
    turtle.forward(side/2)
    turtle.fillcolor('yellow')
    turtle.end_fill()

    #square 4
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(side/4)
    turtle.left(45)
    turtle.forward((side/2) * (2 ** .5) /2) 
    turtle.left(90)
    turtle.forward((side/2) * (2 ** .5) /2) 
    turtle.left(90)   
    turtle.forward((side/2) * (2 ** .5) /2) 
    turtle.left(90)   
    turtle.forward((side/2) * (2 ** .5) /2) 
    turtle.left(90)   
    turtle.fillcolor('red')
    turtle.end_fill()

    #square 5
    turtle.begin_fill()
    turtle.forward((side/2) * (2 ** .5) /4)
    turtle.left(45)
    turtle.forward(side/4)
    turtle.left(90)
    turtle.forward(side/4)
    turtle.left(90)
    turtle.forward(side/4)
    turtle.left(90)
    turtle.forward(side/4)
    turtle.left(90)
    turtle.fillcolor('orange')
    turtle.end_fill()

    #square 6
    turtle.begin_fill()
    turtle.forward(side/8)
    turtle.left(45)
    turtle.forward((side/4) * (2 ** .5) /2)
    turtle.left(90)
    turtle.forward((side/4) * (2 ** .5) /2)
    turtle.left(90)
    turtle.forward((side/4) * (2 ** .5) /2)
    turtle.left(90)
    turtle.forward((side/4) * (2 ** .5) /2)
    turtle.left(90)
    turtle.fillcolor('purple')
    turtle.end_fill()
    
    (input('Press key to continue'))

    
    

def main():
    draw_squares(750)
    print('The side length of the smallest square is : ', )


if __name__ == '__main__':
    main()
