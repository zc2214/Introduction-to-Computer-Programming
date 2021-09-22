import turtle
import math

def main():
    p = int(turtle.numinput("Star polygon", 'Number of vertices?'))
    q = int(turtle.numinput("Star polygon", 'Density?',minval=1,maxval=p//2))
    radius = int(turtle.numinput("Star polygon", 'Radius in pixels? (maximum 250)',minval=1,maxval=250))

    turtle_init(radius)
    
    turtle.color('blue','green')
    filled_reg_star_polygon(p, q, radius)

def reg_star_polygon(p, q, R):
    angle = (p - 2 * q) * 180 / p
    length = 2 * R * math.sin(q * math.pi / p)

    turtle.tracer(0)

    turtle.penup()
    turtle.goto(R,0)
    turtle.setheading(180 - angle / 2)
    turtle.pendown()

    for i in range(p):
        turtle.forward(length)
        turtle.left(180 - angle)
        
    turtle.update()

def filled_reg_star_polygon(p, q, R):
    turtle.penup()
    turtle.goto(R,0)
    turtle.begin_fill()
    reg_star_polygon(p, q, R)
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
