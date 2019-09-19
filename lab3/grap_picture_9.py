from graph import *

def ellipse_filled(x, y, x1, y1, a):
	for i in range(min(x1, x) - a, max(x1, x) + a, ++1):
		for j in range(min(y1, y) - a, max(y1, y) + a, ++1):
			if ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 <= a:
				point(i,j)
				
def ellipse_simple(x, y, x1, y1, a, fat):
	for i in range(min(x1, x) - a, max(x1, x) + a, ++1):
		for j in range(min(y1, y) - a, max(y1, y) + a, ++1):
			if ((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 >= a - fat and \
			((x-i)**2 + (y-j)**2) **0.5 + ((x1-i) **2 + (y1-j) **2) **0.5 <= a + fat:
				point(i,j)
	

penColor("cyan")
brushColor("cyan")
rectangle(-1,-1,500,320)
penColor("black")
brushColor(230,230,230)
rectangle(0,321,500,600)
penColor(180,255,255-44)
penSize(30)
brushColor("cyan")
circle(300,100,130)
line(165,97,435,103)
line(310,-30,290,235)
penColor(220,255,255-46)
line(155,97,185,98)
line(415,102,445,103)
line(285,99,315,101)
line(275,230,305,230)

penColor(250,250,200)
penSize(1)
brushColor(250,250,200)
ellipse_filled(288,100,318,100,50)
ellipse_filled(163,97,177,97,20)
ellipse_filled(423,102,437,102,20)
ellipse_filled(290,223,290,237,20)

run()
