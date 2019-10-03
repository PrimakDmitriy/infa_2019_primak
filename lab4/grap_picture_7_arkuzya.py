from graph import*
import random

rand1 = random.random() * random.random() * 15  #random_shape_for_ghosts
rand2 = random.random() * random.random() * 15
rand3 = random.random() * random.random() * 15

penColor(150,150,150) #фон
brushColor(150,150,150)
rectangle(0,0,470,600)
brushColor(0,0,0)
penColor(0,0,0)
rectangle(0,280,470,700)

brushColor(255, 255, 255)#луна
penColor(150, 150, 150)
circle(390, 60, 40)

def oblako(x,y,a,b,clr1,clr2,clr3):
    penColor(clr1,clr2,clr3)
    brushColor(clr1,clr2,clr3)
    moveTo(x-a,y-b)
    X=-a
    Y=-b
    for i in range (2*b):
        for ii in range (2*a):
            if X**2/a**2+Y**2/b**2<=1:
                point(x+X,y+Y)
            X=X+1
            moveTo(X+x,Y+y)
        X=-a
        Y=Y+1
        moveTo(x-a,y+Y)

def house(x,y):

    brushColor(40,34,11) #дом
    penColor(40,34,11)
    rectangle(x,y,x+120,y+180)

    brushColor(43,17,0) #окна низ
    penColor(43,17,0)
    rectangle(x+12,y+135,x+36,y+165)
    rectangle(x+48,y+135,x+72,y+165)
    brushColor("yellow")
    penColor("yellow")
    rectangle(x+84,y+135,x+108,y+165)

    brushColor(72,62,55) #окна верх
    penColor(72,62,55)
    rectangle(x+12,y,x+27,y+90)
    rectangle(x+39,y,x+54,y+90)
    rectangle(x+66,y,x+81,y+90)
    rectangle(x+93,y,x+108,y+90)

    brushColor(26,26,26) #балкон
    penColor(26,26,26)
    rectangle(x-10,y+80,x-5+135,y+98)
    rectangle(x-10+3,y+60,x-5+132,y+65)
    rectangle(x-10+1,y+65,x-10+3,y+80)
    rectangle(x-10+133,y+65,x-10+135,y+80)
    rectangle(x+4,y+65,x+12,y+80)
    rectangle(x+30,y+65,x+38,y+80)
    rectangle(x+56,y+65,x+64,y+80)
    rectangle(x+82,y+65,x+90,y+80)
    rectangle(x+106,y+65,x+114,y+80)

    brushColor(0,0,0) #крыша
    penColor(0,0,0)
    polygon([(x-10,y+10),(x+130,y+10),(x+118,y-5),(x+2,y-5)])

    brushColor(26,26,26) #трубы на крыше
    penColor(26,26,26)
    rectangle(x+24,y+4,x+27,y-14)
    rectangle(x+33,y+6,x+39,y-20)
    rectangle(x+79,y-3,x+81,y-14)
    rectangle(x+106,y+6,x+108,y-14)

house(157,213)
oblako(150,360,95,17,42,42,42)
house(10,290)
oblako(320,150,125,20,26,26,26)
house(320,132)
oblako(190,80,170,20,51,51,51)
oblako(315,65,125,20,77,77,77)
oblako(375,105,105,15,77,77,77)
oblako(330,310,110,15,40,40,40)

#ПРИВИДЕНИЯ О УЖАС

X = 400 #привидение большое
Y = 470
R = 25
brushColor(179,179,179)
penColor(179,179,179)
polygon([(X-R,Y),(X-R-40+2*rand2,Y+38),(X-R-36,Y+40),(X-R-23,Y+35),(X-R-20,Y+35),(X-R-12,Y+40),(X-R-8,Y+40),(X-R+13+2*rand1,Y+50),(X-R+17+2*rand1,Y+50),(X-R+30,Y+30+2*rand3),(X-R+33,Y+29+2*rand3),(X-R+50,Y+35),(X-R+56,Y+40),(X-R+60,Y+38-rand3),(X+R,Y)])
circle(X,Y,R)
brushColor(135,202,222)
penColor(135,202,222)
circle(X-10,Y,4)
circle(X+10,Y-3,4)
brushColor(0,0,0)
penColor(0,0,0)
circle(X-11,Y,1)
circle(X+9,Y-3,1)

def samayayzhasnayafignya (X,Y): #МАЛЕНЬКИЕ СПРАВА
    brushColor(179,179,179)
    penColor(179,179,179)
    circle(X,Y,12)
    polygon([(X - 12, Y), (X - 20, Y + 13), (X - 28, Y + 25), (X - 26, Y + 22),\
     (X - 25, Y + 20 + rand1), (X - 23, Y + 25), (X - 22, Y + 30), (X - 17, Y + 37),\
      (X - 15, Y + 38), (X - 10, Y + 38 + rand2), (X, Y + 30), (X + 5, Y + 28), (X + 10, Y + 33),\
       (X + 12, Y + 32), (X + 15, Y + 30), (X + 17, Y + 22), (X + 18, Y + 20), (X + 16, Y + 10),\
        (X + 12, Y)])
    brushColor(135,202,222)
    penColor(135,202,222)
    circle(X-5,Y,3)
    circle(X+5,Y-1,3)
    brushColor(0,0,0)
    penColor(0,0,0)
    circle(X-6,Y,1)
    circle(X+4,Y-1,1)

samayayzhasnayafignya(405,360)
samayayzhasnayafignya(425,390)
samayayzhasnayafignya(350,460)

def samayayzhasnayafignya (X,Y): #МАЛЕНЬКИЕ СЛЕВА
    brushColor(179,179,179)
    penColor(179,179,179)
    circle(X,Y,12)
    polygon([(X - 12, Y), (X - 28, Y + 25), (X - 25, Y + 22), (X - 20, Y + 30), (X - 19, Y + 36),\
     (X - 16, Y + 38), (X - 14, Y + 38), (X - 10, Y + 25 + rand1), (X - 8, Y + 25 + rand1),\
      (X, Y + 30), (X + 10, Y + 33), (X + 14, Y + 30), (X + 15, Y + 25), (X + 17 - rand2, Y + 20),\
       (X + 12, Y)])
    brushColor(135,202,222)
    penColor(135,202,222)
    circle(X-5,Y,3)
    circle(X+5,Y-1,3)
    brushColor(0,0,0)
    penColor(0,0,0)
    circle(X-4,Y,1)
    circle(X+6,Y-1,1)

samayayzhasnayafignya(80,500)
samayayzhasnayafignya(100,520)

run()
