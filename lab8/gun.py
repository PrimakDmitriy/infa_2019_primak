from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 3
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def move(self, obj):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        self.y += self.vy
        self.vy += self.ay
        if self.y >= 590 - self.r:
            self.vy = 0
            self.y = 590 - self.r
        canv.move(self.id, self.vx, self.vy)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        return ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 < self.r + obj.r


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...
    
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0,0,0,0)
        x = self.x = rnd(400, 780)
        y = self.y = rnd(100, 500)
        r = self.r = rnd(10, 50)
        color = self.color = 'yellow'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
    
    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
    
    def move(self, speed = 1):
        if self.x <= 350 or self.x + self.r >= 800:
            speed *= -1
        canv.move(self.id, speed, 0)
        root.after(20, move(speed))


g1 = Gun()
screen1 = canv.create_text(400, 300, text='', font='28')
score = 0
score_screen = canv.create_text(30, 30, text='Score: ' + str(score), justify = 'left')

def stop_game():
    exit()

def new_game(event=''):
    global t1, t2, screen1, g1, balls, bullet, score
    t1 = Target()
    t2 = Target()
    balls = []
    bullet = 0
    canv.itemconfig(screen1, text='')
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    t1.live = 1
    t2.live = 1
    t1.move(0.01 * t1.r ** 2)
    t2.move(0.01 * t2.r ** 2)
    while t1.live or t2.live or balls:
        if bullet > 10:
            over = 1
            break
        else:
            over = 0
        for b in balls:
            b.move(g1)
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                score += 1000000 // t1.r ** 2 // bullet
                canv.itemconfig(score_screen, text='Score: ' + str(score))
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                score += 1000000 // t1.r ** 2 // bullet
                canv.itemconfig(score_screen, text='Score: ' + str(score))
        if not t1.live and not t2.live:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            if bullet / 10 % 10 == 1:
                ending = 'ов'
            elif bullet % 10 == 1:
                ending = ''
            elif bullet % 10 >= 2 and bullet % 10 <= 4:
                ending = 'а'
            else:
                ending = 'ов'
            canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрел' + ending)
            break
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.delete(Gun)
    canv.delete(t1.id)
    canv.delete(t2.id)
    for bb in balls:
        canv.delete(bb.id)
    if not over:
        root.after(1500, new_game)
    else:
        canv.itemconfig(screen1, text = 'Игра окончена. Очки: %s' %score)
        time.sleep(2)
        stop_game()


new_game()

mainloop()
