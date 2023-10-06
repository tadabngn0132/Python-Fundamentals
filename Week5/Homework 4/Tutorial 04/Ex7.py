import turtle as t
t. speed(0)

def circle_at(x, y, r, colour):
    # for i in range(5):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t. setheading(0)
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

circle_at(0, 0, 100, 'white')
circle_at(0, 0, 80, 'black')
circle_at(0, 0, 60, 'blue')
circle_at(0, 0, 40, 'red')
circle_at(0, 0, 20, 'yellow')

t.exitonclick()