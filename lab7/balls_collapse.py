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
	
	def move(self):
		canv.move(str(self.tag), self.speed.x, self.speed.y)
		self.coords.x += self.speed.x
		self.coords.y += self.speed.y
	
	def reflect(self, canv_width, canv_height):
		if self.coords.x + self.radius >= canv_width or self.coords.x - self.radius <= 0:
			self.speed.x *= -1
		if self.coords.y + self.radius >= canv_width or self.coords.y - self.radius <= 0:
			self.speed.y *= -1

def new_ball():
    canv.delete('text1')
    global maxelem, tagcount
    global x, y, balls
    if len(balls) < maxelem:
        global pause_time
        ux = int(rnd(-10,10))
        uy = int(rnd(-10,10))
        r = rnd(30,50)
        tagball = 'ball'+ str(tagcount)
        tagcount += 1
        col = choice(colors)
        balls.append(Ball(x, y, r, ux, uy, 0, 0, col, tagball))
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
    clicked = 0
    i = 0
    while i < len(balls):
        if (balls[i].coords.x - x_click) ** 2 + (balls[i].coords.y - y_click) ** 2 < balls[i].radius ** 2:
            clicked += 1
            canv.delete(str(balls[i].tag))
            balls.pop(i)
        else:
            i += 1


def update():
    global balls
    for i in range(int(len(balls))):
        balls[i].reflect(2 * x, 2 * y)
        balls[i].move()
    canv.delete('text')
    canv.create_text(720, 20, text="Balls: %s" % (len(balls)), justify=RIGHT, font="Verdana 14", tag='text')
    root.after(50,update)

balls = []

pause_time = 3000
maxelem = 12
tagcount = 0
x = 400
y = 300

new_ball()
update()
canv.bind('<Button-1>', click)
mainloop()
