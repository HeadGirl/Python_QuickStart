# coding : utf-8

import turtle
import random
import math

import mrrobot

PHI = 360/7
R = 50

def gotoxy(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

def draw_circle(r, color):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

def draw_drum(x0, y0):
	#основной круг
	gotoxy(x0,y0)
	turtle.circle(80)  #барабан
	#мушка
	gotoxy(x0,160 + y0)
	draw_circle(5, "red")
	#барабан
	for i in range(0,7):
		phi_rad = PHI * i * math.pi / 180.0
		gotoxy(x0 + math.sin(phi_rad) * R, y0 + math.cos(phi_rad) * R + 60)
		draw_circle(22, "white")

def draw_rot(x0, y0, start):
	for i in range(start,random.randrange(7,100)):
		phi_rad = PHI * i * math.pi / 180.0
		gotoxy(x0 + math.sin(phi_rad) * R, y0 + math.cos(phi_rad) * R + 60)
		draw_circle(22, "brown")
		draw_circle(22, "white")
	gotoxy(x0 + math.sin(phi_rad) * R, y0 + math.cos(phi_rad) * R + 60)
	draw_circle(22, "brown")
	return i % 7

turtle.speed(0) 
draw_drum(0, 0)

answer = ''
start = 0

while answer != 'N':
	answer = turtle.textinput("Играть?", "Y/N")
	if answer == 'Y':
		#пуля
		start = draw_rot(0, 0, start)
	
		if start == 0:
			gotoxy(-150, 250)
			turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))
			i = random.randrange(0,2)
			print(i)
			if i == 1:
				mrrobot.duble_files('./test/')
			elif i == 0:
				mrrobot.del_ran_file('./test/')
			else:
				print('Что-то пошло не так....')
	else:
		pass