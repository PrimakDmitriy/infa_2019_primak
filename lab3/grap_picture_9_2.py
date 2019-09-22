from graph import *

def ellipse_filled(x, y, x1, y1, a):
        x = int(x)
        y = int(y)
        x1 = int(x1)
        y1 = int(y1)
        a = int(a)
        for i in range(min(x1, x) - a, max(x1, x) + a, ++ 1):
                for j in range(min(y1, y) - a, max(y1, y) + a, ++ 1):
                        if ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 <= a:
                                point(int(i), int(j))
                        
def ellipse_simple(x, y, x1, y1, a, bold):
        x = int(x)
        y = int(y)
        x1 = int(x1)
        y1 = int(y1)
        a = int(a)
        bold = int(bold)
        for i in range(min(x1, x) - a, max(x1, x) + a, ++ 1):
                for j in range(min(y1, y) - a, max(y1, y) + a, ++ 1):
                        if ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 >= a - bold and \
                           ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 <= a + bold:
                                point(int(i), int(j))
                                
def bear(x, y, size, reverseX, reverseY):
    s = 1 / size
    a = reverseX
    b = reverseY
    penColor ("black")    #rode and icehole
    penSize (3//s)
    moveTo (x+140//s*a, y+360//s*b)
    lineTo (x+170//s*a, y+320//s*b)
    lineTo (x+205//s*a, y+290//s*b)
    lineTo (x+255//s*a, y+242//s*b)
    lineTo (x+317//s*a, y+200//s*b)
    lineTo (x+380//s*a, y+165//s*b)
    penSize (1)
    ellipse_simple (x+420//s*a, y+450//s*b, x+280//s*a, y+450//s*b, 150//s, 1)
    penColor (70,60,60)
    ellipse_filled (x+420//s*a, y+450//s*b, x+280//s*a, y+450//s*b, 150//s)
    penColor ("black")
    ellipse_simple (x+415//s*a, y+458//s*b, x+285//s*a, y+458//s*b, 135//s, 1)
    penColor (0,75,20)
    ellipse_filled (x+415//s*a, y+458//s*b, x+285//s*a, y+458//s*b, 135//s)
    penColor ("black")
    line (x+380//s*a, y+452//s*b, x+380//s*a, y+165//s*b)
    
    penColor ("black")          #bear without icehole and face
    ellipse_simple (x+70//s*a, y+230//s*b, x+150//s*a, y+230//s*b, 89//s, 1)
    penColor (230, 230, 230)
    ellipse_filled (x+70//s*a, y+230//s*b, x+150//s*a, y+230//s*b, 89//s)
    penColor ("black")
    ellipse_simple (x+70//s*a, y+260//s*b, x+70//s*a, y+470//s*b, 251//s, 1)
    penColor (230, 230, 230)
    ellipse_filled (x+70//s*a, y+260//s*b, x+70//s*a, y+470//s*b, 251//s)
    penColor ("black")
    ellipse_simple (x+126//s*a, y+317//s*b, x+180//s*a, y+317//s*b, 59//s, 1)
    ellipse_simple (x+90//s*a, y+460//s*b, x+165//s*a, y+460//s*b, 105//s, 1)
    penColor (230, 230, 230)
    ellipse_filled (x+126//s*a, y+317//s*b, x+180//s*a, y+317//s*b, 59//s)
    ellipse_filled (x+90//s*a, y+460//s*b, x+165//s*a, y+460//s*b, 105//s)
    penColor ("black")
    ellipse_simple (x+140//s*a, y+493//s*b, x+210//s*a, y+493//s*b, 76//s, 1)
    penColor (230, 230, 230)
    ellipse_filled (x+140//s*a, y+493//s*b, x+210//s*a, y+493//s*b, 76//s)
    
    penColor ("black")    #bear's face
    penSize (1)
    moveTo (x+100//s*a, y+240//s*b)
    lineTo (x+130//s*a, y+240//s*b)
    lineTo (x+142//s*a, y+239//s*b)
    lineTo (x+150//s*a, y+236//s*b)
    lineTo (x+155//s*a, y+233//s*b)
    brushColor ("black")
    circle (x+154//s*a, y+225//s*b, 2//s)
    circle (x+108//s*a, y+220//s*b, 2//s)
    brushColor (230, 230, 230)
    polygon ([(x+84//s*a, y+219//s*b), (x+83//s*a, y+216//s*b), (x+80//s*a, y+214//s*b), (x+76//s*a, y+213//s*b), (x+74//s*a, y+213//s*b),\
    (x+72//s*a, y+213//s*b), (x+71//s*a, y+215//s*b), (x+70//s*a, y+218//s*b), (x+71//s*a, y+221//s*b), (x+73//s*a, y+224//s*b),\
               (x+77//s*a, y+225//s*b), (x+84//s*a, y+219//s*b)])

def fish(x, y, size, reverseX, reverseY):
        s = 1 / size
        a = reverseX
        b = reverseY
        brushColor (150, 170, 150)    #fish
        penColor ("black")
        polygon ([(x+350//s*a, y+535//s*b), (x+335//s*a, y+550//s*b), (x+324//s*a, y+538//s*b), \
                  (x+332//s*a, y+538//s*b), (x+343//s*a, y+537//s*b), (x+350//s*a, y+535//s*b)])
        polygon ([(x+350//s*a, y+535//s*b), (x+360//s*a, y+525//s*b), (x+370//s*a, y+517//s*b), (x+380//s*a, y+512//s*b), \
                  (x+390//s*a, y+510//s*b), (x+400//s*a, y+510//s*b), (x+410//s*a, y+513//s*b), (x+420//s*a, y+518//s*b), \
                  (x+415//s*a, y+524//s*b), (x+410//s*a, y+528//s*b), (x+400//s*a, y+532//s*b), (x+390//s*a, y+534//s*b), \
                  (x+380//s*a, y+536//s*b), (x+370//s*a, y+536//s*b), (x+360//s*a, y+535//s*b), (x+350//s*a, y+535//s*b)])
        brushColor (170, 0, 220)
        penColor (140, 0, 200)
        circle (x+405//s*a, y+520//s*b, 4//s)
        penColor (230, 230, 230)
        penSize (2//s)
        line (x+405//s*a, y+520//s*b, x+402//s*a, y+519//s*b)
        penSize (1)
        penColor ("black")
        brushColor (255, 100, 100)
        polygon ([(x+395//s*a, y+510//s*b), (x+395//s*a, y+504//s*b), (x+393//s*a, y+501//s*b), (x+390//s*a, y+500//s*b), \
                  (x+360//s*a, y+509//s*b), (x+367//s*a, y+510//s*b), (x+370//s*a, y+512//s*b), (x+375//s*a, y+514//s*b), \
                  (x+383//s*a, y+512//s*b), (x+388//s*a, y+511//s*b), (x+391//s*a, y+510//s*b), (x+395//s*a, y+510//s*b)])
        polygon ([(x+375//s*a, y+536//s*b), (x+365//s*a, y+535//s*b), (x+364//s*a, y+540//s*b), (x+361//s*a, y+543//s*b), \
                  (x+378//s*a, y+541//s*b), (x+378//s*a, y+538//s*b), (x+375//s*a, y+536//s*b)])
        polygon ([(x+399//s*a, y+532//s*b), (x+396//s*a, y+533//s*b), (x+397//s*a, y+540//s*b), (x+401//s*a, y+545//s*b), \
                  (x+407//s*a, y+546//s*b), (x+414//s*a, y+536//s*b), (x+407//s*a, y+535//s*b), (x+399//s*a, y+532//s*b)])

penColor ("cyan")   #sky and ground
brushColor ("cyan")
rectangle (-1, -1, 500, 320)
penColor ("black")
brushColor (230, 230, 230)
rectangle (0, 321, 500, 600)

penColor (180, 255, 210)    #polar lights
penSize (30)
brushColor ("cyan")
circle (300, 100, 130)
penSize (20)
line (165, 97, 435, 103)
line (310, -30, 290, 235)
penColor (220, 255, 210)
line (155, 97, 185, 98)
line (415, 102, 445, 103)
line (285, 99, 315, 101)
penSize (30)
line (275, 230, 305, 230)

penColor (250, 250, 200)    #polar lights additional
penSize (1)
brushColor (250, 250, 200)
ellipse_filled (163, 97, 177, 97, 20)
ellipse_filled (423, 102, 437, 102, 20)
ellipse_filled (290, 223, 290, 237, 20)
penSize (2)
brushColor ("cyan")
i = 25
for i in range (13, 1, -1):
    penColor (250-10*i, 250, 200+2*i)
    brushColor (250-10*i, 250, 200+2*i)
    circle (300, 100, 10+i)
    circle (170, 97, 10+i)
    circle (430, 102, 10+i)
    circle (290, 230, 10+i)


bear (0, 400, 1/3, 1, 1)
bear (500, 270, 1/4, -1, 1)
bear (400, 320, 1/3, -1, 1)
bear (500, 370, 1/2, -1, 1)
bear (130, 300, 1/6, 1, 1)
bear (40, 310, 1/10, 1, 1)
fish (-40, 400, 1/3, 1, 1)
fish (200, 300, 1/2, 1, 1)
fish (170, 310, 1/4, 1, 1)
fish (140, 300, 1/2, 1, 1)
fish (125, 425, 1/10, -1, -1)
fish (135, 422, 1/10, -1, -1)
fish (111, 420, 1/10, -1, -1)
fish (117, 420, 1/10, -1, -1)
fish (125, 410, 1/10, -1, -1)
fish (310, 500, 1/4, -1, -1)
fish (400, 580, 1/4, -1, -1)
fish (360, 500, 1/4, 1, -1)
fish (510, 270, 1/4, -1, 1)
fish (340, 210, 1/3, -1, 1)
fish (250, 750, 1/3, 1, -1)
fish (10, 710, 1/3, 1, -1)

run()
