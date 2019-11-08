from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

class Vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

class Ball:
	def __init__(self, x, y, r, ux, uy, ax, ay):
		self.coords = Vector(x, y)
		self.radius = r
		self.speed = Vector(ux, uy)
		self.accel = Vector(ax, ay)
	
	def move(self):
		canv.move(self.id, int(self.speed.x), int(self.speed.y))
		self.coords.x += int(self.speed.x)
		self.coords.y += int(self.speed.y)
		self.speed.x += self.accel.x
		self.speed.y += self.accel.y
	
	def reflect(self, canv_width, canv_height):
		if self.coords.x + self.radius >= canv_width - 10 or self.coords.x - self.radius <= 10:
			self.speed.x *= -1
		if self.coords.y + self.radius >= canv_height - 10 or self.coords.y - self.radius <= 10:
			self.speed.y *= -1

class RedBall(Ball):
        def __init__(self, x, y, r, ux, uy, ax, ay):
                Ball.__init__(self, x, y, r, ux, uy, ax, ay)
                self.color = 'red'
                self.id = canv.create_oval( x-r, y-r, x+r, y+r, fill = self.color, width=0)

class BlackBall(Ball):
        def __init__(self, x, y, r, ux, uy, ax, ay):
                Ball.__init__(self, x, y, r, ux, uy, ax, ay)
                self.color = 'black'
                self.id = canv.create_oval( x-r, y-r, x+r, y+r, fill = self.color, width=0)

def new_red_ball():
    canv.delete('text1')
    global maxelem
    global balls, canv_width, canv_height
    if len(red_balls) < maxelem:
        global pause_time
        ux = int(rnd(-5,5))
        uy = int(rnd(-5,5))
        if ux == 0:
                ux = 1
        r = rnd(20,50)
        red_balls.append(RedBall(rnd(100, canv_width-100), rnd(100, canv_height-100), r, ux, uy, 0, 0))
    root.after(int(pause_time),new_red_ball)

def new_black_ball():
    canv.delete('text1')
    global maxelem
    global balls, canv_width, canv_height
    if len(black_balls) < maxelem:
        global pause_time
        ux = int(rnd(-3,3))
        uy = int(rnd(-3,3))
        r = rnd(20,50)
        black_balls.append(BlackBall(rnd(100, canv_width-100), rnd(100, canv_height-100), r, ux, uy, 0, 0))
    root.after(int(pause_time / 3),new_black_ball)

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
        for i in red_balls:
                if (i.coords.x - x_click) ** 2 + (i.coords.y - y_click) ** 2 < i.radius ** 2:
                        canv.delete(str(i.tag))
                        red_balls.remove(i)
        for i in black_balls:
                if (i.coords.x - x_click) ** 2 + (i.coords.y - y_click) ** 2 < i.radius ** 2:
                        canv.delete(str(i.tag))
                        black_balls.remove(i)

def update():
        global balls, canv_width, canv_height
        global maxelem
        for i in red_balls:
                for j in black_balls:
                        delta_x = (i.coords.x - j.coords.x)
                        delta_y = (i.coords.y - j.coords.y)
                        delta_r = (delta_x ** 2 + delta_y ** 2) ** 0.5 - i.radius - j.radius
                        if  delta_r < 0 and not (delta_x == 0 and delta_y == 0):
                                black_balls.remove(j)
                                canv.delete(j.id)
        colligion = 0
        for i in black_balls:
                for j in black_balls:
                        delta_x = (i.coords.x - j.coords.x)
                        delta_y = (i.coords.y - j.coords.y)
                        delta_r = (delta_x ** 2 + delta_y ** 2) ** 0.5 - i.radius - j.radius
                        if  delta_r < 0 and not (delta_x == 0 and delta_y == 0) and i != j:
                                i.speed.x *= -1
                                i.speed.y *= -1
                                j.speed.x *= -1
                                j.speed.y *= -1
                                colligion = 1
                                break
                if colligion:
                        break
        if colligion and len(black_balls) < maxelem:
                black_balls.append(BlackBall(rnd(100, canv_width-100), rnd(100, canv_height-100), i.radius, -i.speed.x, -i.speed.y, 0, 0)) 

        for i in red_balls:
                i.reflect(canv_width, canv_height)
                i.move()
        for i in black_balls:
                i.reflect(canv_width, canv_height)
                i.move()
        canv.delete('text')
        canv.create_text(720, 20, text="Balls: %s" % (len(red_balls)+len(black_balls)), justify=RIGHT, font="Verdana 14", tag='text')
        root.after(20,update)

red_balls = []
black_balls = []

pause_time = 3000
maxelem = 6
canv_width = 800
canv_height = 600

new_red_ball()
new_black_ball()
update()
canv.bind('<Button-1>', click)
mainloop()
