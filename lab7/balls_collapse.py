from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue','cyan','black','magenta','violet','grey']

def new_ball():
    canv.delete('text1')
    global maxelem, tagcount
    global ball_dx, ball_dy, ball_x, ball_y, ball_r, x, y
    if len(ball_x) < maxelem:
        global pause_time
        dx = int(rnd(-10,10))
        dy = int(rnd(-10,10))
        r = rnd(30,50)
        tagball = 'ball'+ str(tagcount)
        tagcount += 1
        canv.create_oval( x+100-r, y-r, x+100+r, y+r, fill = choice(colors), width=0, tag=tagball )
        ball_dx.append(dx)
        ball_dy.append(dy)
        ball_x.append(x + 100)
        ball_y.append(y)
        ball_r.append(r)
        ball_tags.append(tagball)
    root.after(int(pause_time),new_ball)

def time_and_speed():
    global pause_time
    if pause_time > 1000:
        pause_time /= 1.01
    root.after(int(pause_time), time_and_speed)

def stop_game():
    exit()

def delete_ball(i):
    ball_dx.pop(i)
    ball_dy.pop(i)
    ball_x.pop(i)
    ball_y.pop(i)
    ball_r.pop(i)
    ball_tags.pop(i)

def click(event):
    x_click = event.x
    y_click = event.y
    clicked = 0
    i = 0
    while i < len(ball_x):
        if (ball_x[i] - x_click) ** 2 + (ball_y[i] - y_click) ** 2 < ball_r[i] ** 2:
            if clicked >= 1:
                canv.create_text(720, 100, text="Cool!", justify=RIGHT, font="Verdana 14", tag='text1')
            clicked += 1
            canv.delete(str(ball_tags[i]))
            delete_ball(i)
        else:
            i += 1


def update():
    global ball_x, ball_y, ball_r, ball_dx, ball_dy
    for i in range(int(len(ball_x))):
        if ball_x[i] + ball_r[i] >= 790 or ball_x[i] - ball_r[i] <= 10:
            ball_dx[i] *= -1
        if ball_y[i] + ball_r[i] >= 590 or ball_y[i] - ball_r[i] <= 10:
            ball_dy[i] *= -1
        canv.move(str(ball_tags[i]), ball_dx[i], ball_dy[i])
        ball_x[i] += ball_dx[i]
        ball_y[i] += ball_dy[i]
    root.after(50,update)

ball_dx = []   #lists
ball_dy = []
ball_x = []
ball_y = []
ball_r = []
ball_tags = []
tagcount = 0

pause_time = 3000
maxelem = 12
x = 400
y = 300

new_ball()
update()
canv.bind('<Button-1>', click)
mainloop()
