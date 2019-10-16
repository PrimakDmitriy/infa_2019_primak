from turtle import *
speed(0)
def poli(i):
	for j in range(i):
		forward(20 * i)
		right(360 / i)

for i in range(3, 13, 1):
	right(90 + 180 / i)
	poli(i)
	left(90 + 180 / i)
	penup()
	forward(23)
	pendown()