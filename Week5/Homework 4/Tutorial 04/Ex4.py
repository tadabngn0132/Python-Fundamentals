import turtle as t

def draw_square(length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

lengths = [40, 60, 80, 100]

for length in lengths:
    draw_square(length)

t.exitonclick()


# import turtle as t

# def draw_square(length):
#     t.forward(length)
#     t.left(90)
#     t.forward(length)
#     t.left(90)
#     t.forward(length)
#     t.left(90)
#     t.forward(length)
#     t.left(90)

# draw_square(40)
# draw_square(60)
# draw_square(80)
# draw_square(100)

# t.exitonclick()