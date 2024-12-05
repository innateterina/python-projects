# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(233, 226, 216), (232, 157, 72), (38, 116, 156), (218, 174, 9), (164, 57, 73), (109, 165, 196), (244, 202, 79), (49, 132, 73), (218, 83, 65), (126, 188, 145), (209, 227, 217), (199, 66, 79), (230, 213, 221), (139, 63, 57), (213, 129, 143),
              (205, 222, 231), (22, 91, 71), (48, 154, 185), (73, 165, 133), (237, 159, 184), (68, 50, 48), (98, 52, 50), (236, 174, 160), (101, 48, 63), (167, 207, 174), (70, 47, 49), (48, 66, 61), (245, 196, 6), (120, 117, 156), (156, 204, 217)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
