from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue','cyan','black','magenta','violet','grey']

class Vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

class Ball:
	def __init__(self, x, y, r, ux, uy, ax, ay, col, tagg):
		self.coords = Vector(x, y)
		self.radius = r
		self.speed = Vector(ux, uy)
		self.accel = Vector(ax, ay)
		self.color = col
		self.tag = tagg
		canv.create_oval( x-r, y-r, x+r, y+r, fill = col, width=0, tag=tagg)
	
	def move(self, energy_dec):
		canv.move(str(self.tag), int(self.speed.x), int(self.speed.y))
		self.coords.x += int(self.speed.x)
		self.coords.y += int(self.speed.y)
		self.speed.x += self.accel.x / energy_dec
		self.speed.y += self.accel.y / energy_dec
	
	def reflect(self, canv_width, canv_height):
		if self.coords.x + self.radius >= canv_width - 10 or self.coords.x - self.radius <= 10:
			self.speed.x *= -1
		if self.coords.y + self.radius >= canv_height - 10 or self.coords.y - self.radius <= 10:
			self.speed.y *= -1

def new_ball():
    canv.delete('text1')
    global maxelem, tagcount
    global balls, canv_width, canv_height
    if len(balls) < maxelem:
        global pause_time
        ux = int(rnd(-5,5))
        uy = int(rnd(-5,5))
        r = rnd(30,50)
        tagball = 'ball'+ str(tagcount)
        tagcount += 1
        col = choice(colors)
        balls.append(Ball(canv_width / 2, canv_height / 2, r, ux, uy, 0, 0, col, tagball))
    root.after(int(pause_time),new_ball)

def time_and_speed():
    global pause_time
    if pause_time > 1000:
        pause_time /= 1.01
    root.after(int(pause_time), time_and_speed)

def stop_game():
    exit()

def click(event):
    x_click = event.x
    y_click = event.y
    i = 0
    while i < len(balls):
        if (balls[i].coords.x - x_click) ** 2 + (balls[i].coords.y - y_click) ** 2 < balls[i].radius ** 2:
            canv.delete(str(balls[i].tag))
            balls.pop(i)
        else:
            i += 1


def update():
	global balls, canv_width, canv_height
	global k_firm, energy_dec
	if len(balls) > 1:
		for i in range(int(len(balls))):
			balls[i].accel.x = 0
			balls[i].accel.y = 0
			for j in range(int(len(balls))):
				if i == j:
					continue
				delta_x = (balls[i].coords.x - balls[j].coords.x)
				delta_y = (balls[i].coords.y - balls[j].coords.y)
				delta_r = (delta_x ** 2 + delta_y ** 2) ** 0.5 - balls[i].radius - balls[j].radius
				if  delta_r < 0 and not (delta_x == 0 and delta_y == 0):
					force = k_firm * (- delta_r) ** 1  #force > 0
					balls[i].accel.x += force * delta_x / (delta_x ** 2 + delta_y ** 2) ** 0.5
					balls[i].accel.y += force * delta_y / (delta_x ** 2 + delta_y ** 2) ** 0.5
	for i in range(int(len(balls))):
		balls[i].reflect(canv_width, canv_height)
		balls[i].move(energy_dec)
	canv.delete('text')
	canv.create_text(720, 20, text="Balls: %s" % (len(balls)), justify=RIGHT, font="Verdana 14", tag='text')
	root.after(20,update)

balls = []

pause_time = 3000
maxelem = 6
tagcount = 0
canv_width = 800
canv_height = 600
k_firm = 1
energy_dec = 22

new_ball()
update()
canv.bind('<Button-1>', click)
mainloop()
