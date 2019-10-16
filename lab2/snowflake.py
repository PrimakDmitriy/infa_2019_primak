from turtle import *
speed(0)
def line(dep):
	print(dep)
	if dep < 11:
		forward(200 / (1.618 ** (dep - 1)))
		left(15)
		line(dep + 1)
		right(30)
		line(dep + 1)
		left(15)
		penup()
		backward(200 / (1.618 ** (dep - 1)))
		pendown()
	
for i in range(6):
	line(1)
	right(60)
exitonclick()