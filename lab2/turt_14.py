from turtle import *
def star(n):
	for i in range(n):
		forward(100)
		left(180 - 180 / n)
	
star(5)
penup()
goto(200, 0)
pendown()
star(11)