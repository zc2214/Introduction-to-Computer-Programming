import turtle
import math

def main():
    n_edges = int(input('Number of sides for the regular polygon?\n> '))
    radius = int(input('Circle radius in pixels? (maximum 250)\n> '))

    turtle_init(radius)
    
    turtle.color('blue','green')
    filled_reg_conv_polygon(n_edges, radius)

def reg_conv_polygon(N, R):
    angle = (N - 2) * 180 / N
    length = 2 * R * math.sin(math.pi / N)

    turtle.tracer(0)

    turtle.penup()
    turtle.goto(R,0)
    turtle.setheading(180 - angle / 2)
    turtle.pendown()

    for i in range(N):
        turtle.forward(length)
        turtle.left(180 - angle)
        
    turtle.update()

def filled_reg_conv_polygon(N, R):
    turtle.penup()
    turtle.goto(R,0)
    turtle.begin_fill()
    reg_conv_polygon(N, R)
    turtle.end_fill()
    turtle.update()

def turtle_init(R):
    turtle.setup(500, 500, 0, 0)
    turtle.hideturtle()
    turtle.tracer(0)

    turtle.color('red','yellow')
    turtle.penup()
    turtle.goto(0,-R)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(R)
    turtle.end_fill()

    turtle.update()

#call the main function
main()
