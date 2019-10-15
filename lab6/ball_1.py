from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue','cyan','black','magenta','violet','grey']

def sign(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return 0

def new_ball():
	global ball_dx, ball_dy, ball_x, ball_y, ball_r, ball_tags
	global pause_time, moving_speed
	dx = int(rnd(6,10) * moving_speed)
	dy = int(rnd(6,10) * moving_speed)
	canv.delete('ball')
	r = rnd(30,50)
	
	canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0, tag='ball')
	root.after(int(pause_time),new_ball)
	
def time_and_speed():
	global pause_time, moving_speed
	if moving_speed < 10:
		moving_speed *= 1.01
	else:
		moving_speed *= 1.001
	if pause_time >= 2000:
		pause_time /= 1.01
	elif pause_time >=1000:
		pause_time /= 1.005
	elif pause_time >= 700:
		pause_time /= 1.002
	elif pause_time >=500:
		pause_time /= 1.001
	elif pause_time >=300:
		pause_time /= 1.0001
	else:
		pause_time /= 1.000001

def click(event):
	global score, errors
	x_click = event.x
	y_click = event.y
	if (x - x_click) ** 2 + (y - y_click) ** 2 < (r + 20) ** 2:
		score += 10 ** 6 / r ** 2
	else:
		errors += 1
	canv.delete('ball')
	canv.delete('text')
	canv.create_text(750, 20, text="Score: %s" % (int(score)), justify=RIGHT, font="Verdana 14", tag='text')
	canv.create_text(750, 40, text="Errors: %s" % (errors), justify=RIGHT, font="Verdana 14", tag='text')
	
def update():
	global dx, dy, x, y, r
	if (x + r >= 790) or (x - r <= 10):
		dx *= -1
	if (y + r >= 590) or (y - r <= 10):
		dy *= -1
	canv.move('ball', dx, dy)
	x += dx
	y += dy
	root.after(50,update)

ball_tags = []    #lists
ball_dx = []
ball_dy = []
ball_x = []
ball_y = []
ball_r = []
triangle_tags = []
triangle_dx = []
triangle_dy = []

score = 0
errors = 0
pause_time = 10000
moving_speed = 1
x = 400
y = 300
dx = 0
dy = 0

canv.create_text(750, 20, text="Score: %s" % (score), justify=RIGHT, font="Verdana 14", tag='text')
canv.create_text(750, 40, text="Errors: %s" % (errors), justify=RIGHT, font="Verdana 14", tag='text')
new_ball()
update()
canv.bind('<Button-1>', click)
mainloop()
