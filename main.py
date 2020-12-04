import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("grey")
turtle.setup(600, 600)
turtle.shape("turtle")

screen = turtle.Screen()

Timmy = turtle.Turtle()

def triangle(length, color):
  Timmy.fillcolor(color)
  Timmy.begin_fill()

  x = 0
  while x < 3:
    Timmy.forward(int(length))
    Timmy.right(120)
    x = x + 1
  Timmy.end_fill()

def circle(length, color):
  Timmy.fillcolor(color)
  Timmy.begin_fill()

  x = 0

  while x < 75:
    Timmy.forward(10)
    Timmy.right(5)
    x = x + 1
  Timmy.end_fill()

def star(length, color):
  Timmy.fillcolor(color)
  Timmy.begin_fill()

  x = 0
  while x < 5:
    Timmy.forward(int(length))
    Timmy.right(145)
    x = x + 1
  Timmy.end_fill()

input_shape = input("What shape do you want to draw? ")
input_length = input("How big: ")
input_color = input("What color? ")

if input_shape == 'triangle':
  triangle(input_length, input_color)
elif input_shape == 'circle':
  circle(input_length, input_color)
elif input_shape == 'star':
  star(input_length, input_color)

turtle.done()