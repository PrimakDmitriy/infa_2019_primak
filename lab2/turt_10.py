from turtle import *
speed(0)
def circle(i):
	for j in range(60):
		forward(i)
		left(6)

k=6
for i in range (k):
	circle(12)
	right(360 / k)
	