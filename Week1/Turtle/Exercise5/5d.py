import turtle as t

length = 100
a = 120
b = 90
t.fillcolor("red")
t.begin_fill()
t.forward(length)
t.left(a)
t.forward(length)
t.left(a)
t.forward(length)
t.left(30)
t.end_fill()
t.fillcolor("yellow")
t.begin_fill()
t.forward(length)
t.left(b)
t.forward(length)
t.left(b)
t.forward(length)
t.left(b)
t.forward(length)
t.left(b*2)
t.end_fill()

t.exitonclick()