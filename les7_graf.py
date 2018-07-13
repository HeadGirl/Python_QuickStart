# coding : utf-8

import turtle
import random
import math


def gotoxy(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

def draw_circle(r, color):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

turtle.speed(0) 
gotoxy(0,0)
turtle.circle(80)  #барабан
gotoxy(0,160)
draw_circle(5, "red") #мушка


phi = 360/7
r = 50

#отрисовка отверстий
for i in range(0,random.randrange(7,100)):
	phi_rad = phi * i * math.pi / 180.0
	gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
	draw_circle(22, "brown")
	draw_circle(22, "white")

#пуля
gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
draw_circle(22, "brown")


if i % 7 == 0:
	gotoxy(-150, 250)
	turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))

answer = ''
while answer != 'N':
	answer = turtle.textinput("Нарисовать окружность", "Y/N")
	if answer == 'Y':
		turtle.penup()
		turtle.goto(random.randrange(-300,300), random.randrange(-200,200))
		turtle.pendown()
		turtle.fillcolor(random.random(),random.random(),random.random())
		turtle.begin_fill()
		turtle.circle(random.randrange(1,100))
		turtle.end_fill()
	else:
		pass