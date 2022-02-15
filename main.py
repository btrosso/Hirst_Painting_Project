import turtle as t
import random
# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# print(colors)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(tuple(color.rgb))
#
# print(rgb_colors)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]


# 10x10 spot painting
# dot_size = 20
# dot_spacing = 50

def new_row(turtle):
    """
    Used to move to a new row.
    :param turtle:
    :return:
    """
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.setheading(0)


def make_dot(turtle, color_pallet):
    """
    Used to make a dot and move to the next spot.
    :param turtle:
    :param color_pallet:
    :return:
    """
    turtle.dot(20, random.choice(color_pallet))
    turtle.forward(50)


tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
tim.pu()
tim.ht()
tim.setposition(-250, -200)
print(tim.position())


# logic to create the grid of dots
row = 10
col = 10
for y in range(col):
    for x in range(row):
        make_dot(turtle=tim, color_pallet=color_list)

    new_row(tim)


# instantiating the screen
screen = t.Screen()
screen.exitonclick()
