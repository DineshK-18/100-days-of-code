from turtle import Turtle, Screen
import colorgram
import random

rgb_colors = []

colors = colorgram.extract('image.jpg',100)
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

kim = Turtle()
screen = Screen()
color_list = [(255, 99, 71), (60, 179, 113), (70, 130, 180), (255, 215, 0), (138, 43, 226), (255, 165, 0), (0, 191, 255), (199, 21, 133), (154, 205, 50), (255, 20, 147), (0, 128, 128), (255, 105, 180), (173, 216, 230), (255, 140, 0), (46, 139, 87), (75, 0, 130), (240, 128, 128), (0, 255, 127), (255, 0, 255), (0, 250, 154), (255, 99, 255), (100, 149, 237), (255, 228, 181), (147, 112, 219), (255, 69, 0), (0, 255, 255), (210, 105, 30), (127, 255, 212), (255, 182, 193), (0, 100, 0), (255, 250, 205), (106, 90, 205), (255, 0, 0), (0, 0, 255)]

screen.colormode(255)
kim.speed('fastest')
def first_row():
    for _ in range(10):
        tup = (random.choice(color_list))
        kim.dot(30, tup)
        kim.penup()
        kim.hideturtle()
        kim.fd(40)
        kim.pendown()
        kim.penup()
    kim.bk(400)

def next_row():
    kim.left(90)
    kim.penup()
    kim.fd(40)
    kim.right(90)

for _ in range(10):
    first_row()
    next_row()
screen.exitonclick()