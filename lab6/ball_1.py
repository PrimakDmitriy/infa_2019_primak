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
    canv.delete('text1')
    global errors, maxerr, tagcount, maxelem
    global ball_dx, ball_dy, ball_x, ball_y, ball_r, x, y
    if errors < maxerr and len(ball_x) < maxelem:
        global pause_time, moving_speed
        dx = int(rnd(-10,10) * moving_speed)
        dy = int(rnd(-10,10) * moving_speed)
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
        canv.delete('text')
        canv.create_text(720, 60, text="Balls: %s" % (len(ball_x)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 80, text="Triangles: %s" % (len(triangle_x)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 20, text="Score: %s" % (int(score)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 40, text="Errors: %s" % (errors), justify=RIGHT, font="Verdana 14", tag='text')
    root.after(int(pause_time),new_ball)

def new_triangle():
    global errors, maxerr, tagcount, maxelem
    global triangle_dx, triangle_dy, triangle_x, triangle_y, triangle_r, x, y
    if errors < maxerr and len(triangle_x) < maxelem:
        if len(triangle_x) > maxelem:
            errors += 1
        global pause_time, moving_speed
        dx = int(rnd(-10,10) * moving_speed)
        dy = int(rnd(-10,10) * moving_speed)
        r = rnd(30,50)
        tagtr = 'triangle'+str(tagcount)
        tagcount += 1
        canv.create_polygon( (x-100, y-r), (x - 100 + int(r*0.866), y + r//2), (x - 100 - int(r*0.866), y + r//2),\
            fill = choice(colors), width=0, tag=tagtr )
        triangle_dx.append(dx)
        triangle_dy.append(dy)
        triangle_x.append(x - 100)
        triangle_y.append(y)
        triangle_r.append(r)
        triangle_tags.append(tagtr)
        canv.delete('text')
        canv.create_text(720, 80, text="Triangles: %s" % (len(triangle_x)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 60, text="Balls: %s" % (len(ball_x)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 20, text="Score: %s" % (int(score)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 40, text="Errors: %s" % (errors), justify=RIGHT, font="Verdana 14", tag='text')
    root.after(int(pause_time),new_triangle)

def time_and_speed():
    global pause_time, moving_speed
    if pause_time > 1000:
        pause_time /= 1.01
    if moving_speed < 3:
        moving_speed *= 1.01
    else:
        moving_speed *= 1.001
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

def delete_triangle(i):
    triangle_dx.pop(i)
    triangle_dy.pop(i)
    triangle_x.pop(i)
    triangle_y.pop(i)
    triangle_r.pop(i)
    triangle_tags.pop(i)

def click(event):
    global score, errors, maxerr
    x_click = event.x
    y_click = event.y
    clicked = 0
    i = 0
    while i < len(ball_x):
        if (ball_x[i] - x_click) ** 2 + (ball_y[i] - y_click) ** 2 < ball_r[i] ** 2:
            score += 10 ** 6 / ball_r[i] ** 2
            if clicked >= 1:
                score += 1000 * clicked
                canv.create_text(720, 100, text="Cool!", justify=RIGHT, font="Verdana 14", tag='text1')
            clicked += 1
            canv.delete(str(ball_tags[i]))
            delete_ball(i)
        else:
            i += 1
    i = 0
    while i < len(triangle_x):
        if (triangle_x[i] - x_click) ** 2 + (triangle_y[i] - y_click) ** 2 < triangle_r[i] ** 2:
            score += 10 ** 6 / triangle_r[i] ** 2 * 2
            if clicked >= 1:
                score += 2000 * clicked
                canv.create_text(720, 100, text="Cool!", justify=RIGHT, font="Verdana 14", tag='text1')
            clicked += 1
            canv.delete(str(triangle_tags[i]))
            delete_triangle(i)
        else:
            i +=1
    if clicked == 0:
        errors += 1

    canv.delete('text')
    canv.create_text(720, 20, text="Score: %s" % (int(score)), justify=RIGHT, font="Verdana 14", tag='text')
    canv.create_text(720, 40, text="Errors: %s" % (errors), justify=RIGHT, font="Verdana 14", tag='text')
    if errors >= maxerr:
        canv.delete(ALL)
        canv.create_text(x, y, text="Game Over. Score: %s" % (int(score)), justify=CENTER, font="Verdana 14", tag='text')
        global highscore
        if score > highscore:
            canv.create_text(x, y + 20, text="New highscore!", justify=CENTER, font="Verdana 14", tag='text')
            highscore_file = open("stats.txt", "w")
            highscore_file.write(str(int(score)))
        else:
            canv.create_text(x, y + 20, text="Highscore: %s" % (int(highscore)), justify=CENTER, font="Verdana 14", tag='text')
        root.after(3000, stop_game)

    else:
        canv.create_text(720, 60, text="Balls: %s" % (len(ball_x)), justify=RIGHT, font="Verdana 14", tag='text')
        canv.create_text(720, 80, text="Triangles: %s" % (len(triangle_x)), justify=RIGHT, font="Verdana 14", tag='text')


def update():
    global errors, maxerr
    if errors < maxerr:
        global ball_x, ball_y, ball_r, ball_dx, ball_dy,\
            triangle_x, triangle_y, triangle_r, triangle_dx, triangle_dy
        for i in range(int(len(ball_x))):
            if ball_x[i] + ball_r[i] >= 790 or ball_x[i] - ball_r[i] <= 10:
                ball_dx[i] *= -1
            if ball_y[i] + ball_r[i] >= 590 or ball_y[i] - ball_r[i] <= 10:
                ball_dy[i] *= -1
            canv.move(str(ball_tags[i]), ball_dx[i], ball_dy[i])
            ball_x[i] += ball_dx[i]
            ball_y[i] += ball_dy[i]
        for i in range(int(len(triangle_x))):
            if triangle_x[i] + triangle_r[i] >= 790 or triangle_x[i] - triangle_r[i] <= 10:
                triangle_dx[i] *= -1
            if triangle_y[i] + triangle_r[i] >= 590 or triangle_y[i] - triangle_r[i] <= 10:
                triangle_dy[i] *= -1
            canv.move(str(triangle_tags[i]), triangle_dx[i], triangle_dy[i])
            triangle_x[i] += triangle_dx[i]
            triangle_y[i] += triangle_dy[i]
    root.after(50,update)

ball_dx = []   #lists
ball_dy = []
ball_x = []
ball_y = []
ball_r = []
ball_tags = []
triangle_dx = []
triangle_dy = []
triangle_x = []
triangle_y = []
triangle_r = []
triangle_tags = []
tagcount = 0

score = 0
errors = 0
maxerr = 5
pause_time = 3000
moving_speed = 1
maxelem = 12
x = 400
y = 300
dx = 0
dy = 0

highscore_file = open("stats.txt", "r")
highscore = int(next(highscore_file))

canv.create_text(720, 20, text="Score: %s" % (score), justify=RIGHT, font="Verdana 14", tag='text')
canv.create_text(720, 40, text="Errors: %s" % (errors), justify=RIGHT, font="Verdana 14", tag='text')
new_ball()
new_triangle()
update()
canv.bind('<Button-1>', click)
mainloop()
