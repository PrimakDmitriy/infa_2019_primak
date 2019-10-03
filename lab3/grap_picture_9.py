from graph import *

def ellipse_filled(x, y, x1, y1, a):
	for i in range(min(x1, x) - a, max(x1, x) + a, ++ 1):
		for j in range(min(y1, y) - a, max(y1, y) + a, ++ 1):
			if ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 <= a:
				point(i,j)
				
def ellipse_simple(x, y, x1, y1, a, bold):
	for i in range(min(x1, x) - a, max(x1, x) + a, ++ 1):
		for j in range(min(y1, y) - a, max(y1, y) + a, ++ 1):
			if ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 >= a - bold and \
			((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 <= a + bold:
				point(i,j)
	

penColor("cyan")   #sky and ground
brushColor("cyan")
rectangle(-1, -1, 500, 320)
penColor("black")
brushColor(230, 230, 230)
rectangle(0, 321, 500, 600)

penColor(180, 255, 210)    #polar lights
penSize(30)
brushColor("cyan")
circle(300, 100, 130)
penSize(20)
line(165, 97, 435, 103)
line(310, -30, 290, 235)
penColor(220, 255, 210)
line(155, 97, 185, 98)
line(415, 102, 445, 103)
line(285, 99, 315, 101)
penSize(30)
line(275, 230, 305, 230)

penColor(250, 250, 200)    #polar lights additional
penSize(1)
brushColor(250, 250, 200)
ellipse_filled(288, 100, 318, 100, 50)
ellipse_filled(163, 97, 177, 97, 20)
ellipse_filled(423, 102, 437, 102, 20)
ellipse_filled(290, 223, 290, 237, 20)

penColor("black")    #rode and icehole
penSize(3)
moveTo(140, 360)
lineTo(170, 320)
lineTo(205, 290)
lineTo(255, 242)
lineTo(317, 200)
lineTo(380, 165)
penSize(1)
ellipse_simple(420, 450, 280, 450, 150, 1)
penColor(70, 60, 60)
ellipse_filled(420, 450, 280, 450, 150)
penColor("black")
ellipse_simple(415, 458, 285, 458, 135, 1)
penColor(0, 75, 20)
ellipse_filled(415, 458, 285, 458, 135)
penColor("black")
line(380, 452, 380, 165)

penColor("black")          #bear without icehole and face
ellipse_simple(70, 230, 150, 230, 89, 1)
penColor(230, 230, 230)
ellipse_filled(70, 230, 150, 230, 89)
penColor("black")
ellipse_simple(70, 260, 70, 470, 251, 1)
penColor(230, 230, 230)
ellipse_filled(70, 260, 70, 470, 251)
penColor("black")
ellipse_simple(126, 317, 180, 317, 59, 1)
ellipse_simple(90, 460, 165, 460, 105, 1)
penColor(230, 230, 230)
ellipse_filled(126, 317, 180, 317, 59)
ellipse_filled(90, 460, 165, 460, 105)
penColor("black")
ellipse_simple(140, 493, 210, 493, 76, 1)
penColor(230, 230, 230)
ellipse_filled(140, 493, 210, 493, 76)

penColor("black")    #bear's face
penSize(1)
moveTo(100, 240)
lineTo(130, 240)
lineTo(142, 239)
lineTo(150, 236)
lineTo(155, 233)
brushColor("black")
circle(154, 225, 2)
circle(108, 220, 2)
brushColor(230, 230, 230)
polygon([(84,219),(83,216),(80,214),(76,213),(74,213),(72,213),\
         (71,215),(70,218),(71,221),(73,224),(77,225),(84,219)])

brushColor(150, 170, 150)      #fish
polygon([(350,535),(335,550),(324,538),(332,538),(343,537),(350,535)])
polygon([(350,535),(360,525),(370,517),(380,512),(390,510),(400,510),(410,513),(420,518),\
         (415,524),(410,528),(400,532),(390,534),(380,536),(370,536),(360,535),(350,535)])
brushColor(170, 0, 220)
penColor(140, 0, 200)
circle(405, 520, 4)
penColor(230, 230, 230)
penSize(2)
line(405, 520, 402, 519)
penSize(1)
penColor("black")
brushColor(255, 100, 100)
polygon([(395,510),(395,504),(393,501),(390,500),(360,509),(367,510),\
         (370,512),(375,514),(383,512),(388,511),(391,510),(395,510)])
polygon([(375,536),(365,535),(364,540),(361,543),(378,541),(378,538),(375,536)])
polygon([(399,532),(396,533),(397,540),(401,545),(407,546),(414,536),(407,535),(399,532)])

run()
