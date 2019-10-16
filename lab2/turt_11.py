from turtle import *
speed(0)
def circle(i):
	for j in range(60):
		forward(i)
		left(6)

left(90)		
for i in range(1, 4, 1):
	circle(2 * i)
	right(180)
	circle(2 * i)
	right(180)