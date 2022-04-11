from turtle import Turtle, Screen
from drawer import *

Scr = Screen()
#Scr.bgpic('MrBlacksTrans.gif') #MrBlacksBACKGROUND.png

T = TurtleControl(0, False)

#86 41     156 198 208
Circles = [(280, 'grey'), (250, 'white'), (208, 'black'), (198, 'white'),(185, 'lightgrey'),
            (156, 'white'),'CLOSED-FORM', (86, 'white')]

for info in Circles:
    if info == 'CLOSED-FORM':
        # The closed-form in the middle
        T.pos.HOME()
        T.Tur.seth(-25)
        T.pos.move(115)
        T.pos.move_up(0)

        line_len = 35
        long_line_len = 95
        T.draw.fill_color('black') #coloring
        for i in range(4):
            if i % 2 == 0:
                long_line_len = 95
            else:
                long_line_len = 110

            T.draw.line(long_line_len)
            T.pos.rotate(55, 'L')
            T.draw.line(line_len)
            T.pos.rotate(30, 'R')
            T.draw.line(line_len)
            T.pos.rotate(65, 'L')

        T.draw.end_fill() #coloring
    else:
        r = info[0]
        color = info[1]
        T.pos.HOME()
        T.draw.fill_color(color) #coloring
        T.draw.move_circle(r)
        T.draw.end_fill() #coloring

#(41, 'red')
T.pos.HOME()
T.draw.outline_color('red') #coloring OUTLINE only
T.draw.move_circle(41)
T.draw.end_fill() #coloring


T.pos.HOME()
#Draw inner Star
for i in range(8):
    T.pos.rotate(45, 'L')

    T.pos.move(41)

    T.pos.SAVE()
    j = 0
    for j in range(3):
        T.draw.fill_color('red') #coloring
        T.pos.LOAD()
        T.draw.line(10*j)
        T.pos.rotate(45, 'R')
        T.draw.semi_circle(15, 60)

    j += 1
    T.pos.LOAD()
    T.draw.line(10*j)
    T.pos.rotate(45, 'R')
    T.draw.semi_circle(10, 90)
    T.pos.rotate(45, 'R')
    T.pos.LOAD()

    T.draw.line(41)
    T.pos.rotate(152, 'L')
    T.draw.end_fill() #coloring

    T.pos.SAVE()

    for j in range(3):
        T.draw.fill_color('red') #coloring
        T.pos.LOAD()
        T.draw.line(15*j)
        T.pos.rotate(45, 'R')
        T.draw.semi_circle(15, 90)
        T.draw.end_fill() #coloring

    T.draw.fill_color('red') #coloring
    T.pos.rotate(197, 'R')
    T.pos.LOAD()

    T.draw.line(57)
    T.pos.rotate(152, 'R')
    T.draw.end_fill() #coloring
    T.pos.HOME()

#The things around the star
for i in range(8):
    T.pos.rotate(28, 'L')
    T.pos.move(70)
    T.pos.rotate(33.75, 'L')


    T.pos.rotate(170, 'L')
    T.pos.SAVE()
    T.draw.semi_circle(-45, 17)
    T.pos.LOAD()
    T.pos.rotate(70, 'R')
    T.draw.semi_circle(-45, 15)

    T.pos.rotate(33.75+45+22 ,'R')
    T.pos.HOME()

#mini circles
for i in range(48):
    T.pos.rotate(7.5, 'L')
    T.pos.move(90)

    T.draw.fill_color('white') #coloring
    T.pos.rotate(30, 'L')
    T.draw.oval(-8)
    T.pos.rotate(30, 'R')
    T.draw.end_fill() #coloring
    T.pos.HOME()

a = 35
b = 40
c = 50
dis = 105 #until start drawing
dir = [a*45 for a in range(8)]
for i in range(len(dir)):
    T.Tur.seth(dir[i])
    T.pos.SAVE()
    if i % 2 == 0:
        a = 35
        b = 40
        c = 50
    else: 
        a = 30
        b = 35
        c = 45
#First Tri
    T.draw.fill_color('grey') #coloring
    T.pos.move(dis)
    T.pos.rotate(55, 'L')
    T.draw.line(a)
    T.pos.rotate(100, 'R')
    T.draw.line(b)
    T.pos.rotate(135, 'R')
    T.draw.line(c)
    T.draw.end_fill() #coloring

#Second Tri
    T.pos.LOAD()
    T.pos.rotate(90, 'R')
    T.pos.move(5) #distance between halfs
    T.pos.rotate(90, 'L')
    
    T.pos.move(dis)
    T.pos.rotate(55, 'R')
    T.draw.line(a)
    T.pos.rotate(100, 'L')
    T.draw.line(b)
    T.pos.rotate(135, 'L')
    T.draw.line(c)
    T.pos.HOME()


a = 25
b = 30
c = 40
dis = 110

dir = [22.5, 64, 113, 155, 203, 246, 292, 335]
for i in range(len(dir)):
    T.Tur.seth(dir[i])
    T.pos.SAVE()
#First Small Tri.
    T.pos.move(dis)
    T.draw.fill_color('grey') #coloring
    T.pos.rotate(50, 'L')
    T.draw.line(a)
    T.pos.rotate(85, 'R')
    T.draw.line(b)
    T.pos.rotate(146, 'R')
    T.draw.line(c)
    T.draw.end_fill() #coloring

     
#Second Small Tri.
    T.pos.LOAD()
    T.pos.move(dis)
    T.pos.rotate(50, 'R')
    T.draw.line(a)
    T.pos.rotate(85, 'L')
    T.draw.line(b)
    T.pos.rotate(141, 'L')
    T.draw.line(c)
    T.pos.HOME()


#  small Curves
T.pos.HOME()
T.pos.SAVE()

for i in range(16):
    T.pos.LOAD()
    T.pos.rotate(i*22.5, 'L')
    T.pos.move(155)
    T.pos.rotate(60, 'L')
    T.draw.semi_circle(100, 45)
    T.pos.rotate(30, 'L')
    T.draw.semi_circle(100, 32)


T.pos.HOME()

#Big blacks (similar to triangles)
T.pos.SAVE()
for i in range(16):
    T.Tur.seth(i*22.5)
    T.pos.move(184)
    T.pos.rotate(45, 'R')

    T.draw.fill_color('black')
    T.draw.line(50)

    T.pos.rotate(90, 'L')
    T.draw.semi_circle(100, 55)

    T.pos.rotate(120, 'L')
    T.draw.line(83)
    T.draw.end_fill()
    T.pos.LOAD()


    T.pos.move_up(12)
    T.Tur.seth(i*22.5)
    T.pos.move(217)
    T.pos.rotate(45, 'L')
    T.draw.fill_color('white')
    T.draw.circle(-17)
    T.draw.end_fill()

    T.pos.LOAD()


#   Big Curves 
T.pos.HOME()
T.pos.SAVE()
for i in range(16):
    T.pos.LOAD()
    T.pos.rotate(i*22.5, 'L')
    T.pos.move(257)

    T.pos.rotate(60, 'L')
    T.draw.semi_circle(100, 35)
    T.pos.rotate(20, 'L')
    T.draw.semi_circle(100, 30)


# circles outside
T.pos.HOME()
T.pos.SAVE()
for i in range(16):
    T.pos.LOAD()
    T.pos.rotate(i*22.5, 'L')
    T.pos.move(257)
    T.pos.move_up(0)
    T.draw.fill_color('white') #coloring
    T.draw.circle(6)
    T.draw.end_fill()

Scr.exitonclick()