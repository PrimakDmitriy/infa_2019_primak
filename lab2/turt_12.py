from turtle import *
speed(0)
def duga(grad, vol):
	for i in range(int(grad / 6)):
		forward(vol)
		right(6)
		
left(90)
for i in range(3):
	duga(180, 6)
	duga(180, 1)