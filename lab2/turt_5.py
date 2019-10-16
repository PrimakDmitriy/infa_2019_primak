from turtle import *
def square(x):
	for i in range (4):
		forward(x)
		left(90)
l = 20
for i in range (1,10,1):
	square(l*i)
	penup()
	right(135)
	forward(l*(2**-0.5))
	pendown()
	left(135)