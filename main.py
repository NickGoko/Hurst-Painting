# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# # print(colors)
# # print(len(colors))
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)  # this for color to accept rgb values


colors_list = [(212, 160, 82), (192, 155, 27), (201, 152, 179), (52, 102, 150), (225, 206, 132),
               (172, 69, 44), (226, 233, 244), (27, 27, 64), (152, 28, 39), (29, 64, 32), (37, 80, 42),
               (159, 51, 61), (141, 161, 183), (144, 32, 25), (71, 100, 74), (149, 169, 152), (196, 89, 72),
               (219, 172, 191),
               (228, 175, 166), (47, 46, 92), (56, 46, 20), (50, 23, 45), (174, 100, 110), (102, 123, 163),
               (180, 187, 214),
               (248, 197, 2), (112, 139, 115)]

screen = Screen()
screen.setup(width=800, height=700)
dots = Turtle()
dots.speed("fastest")
# print(dots.pos())


def random_color():
    random_colors = (random.choice(colors_list))
    return random_colors


random_color()
dots.penup()
dots.goto(-200, -250)
dots.hideturtle() 
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    # dots.color(random_color())
    dots.dot(20, random_color())
    dots.forward(50)
    if dot_count % 10 == 0:
        dots.setheading(90)
        dots.forward(50)
        dots.setheading(180)
        dots.forward(500)
        dots.setheading(0)



screen.exitonclick()
