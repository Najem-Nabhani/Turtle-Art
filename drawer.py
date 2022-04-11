from turtle import Turtle


class TurtleControl:
    def __init__(self, speed, visiblity = True):
        self.Tur = Turtle()
        self.Tur.seth(0)
        self.Tur.speed(speed)
        self.Tur.shape("turtle")
        self.Tur.color('black', 'green')

        if not visiblity:
            self.Tur.hideturtle()
        
        self.pos = self.motionControl(self.Tur)
        self.pos.HOME()
        self.draw = self.artControl(self.Tur)

    class motionControl:
        CENTER_X = 5
        CENTER_Y = -8
        sav_x = 5
        sav_y = -8
        sav_ang = 0

        def __init__(self, Tur):
            self.tur = Tur
        
        def HOME(self):
            self.tur.up()
            self.tur.goto(self.CENTER_X, self.CENTER_Y)
            self.tur.down()

        def SAVE(self):
            self.sav_x = self.tur.xcor()
            self.sav_y = self.tur.ycor()
            self.sav_ang = self.tur.heading()

        def LOAD(self):
            self.tur.up()
            self.tur.goto(self.sav_x, self.sav_y)
            self.tur.seth(self.sav_ang)
            self.tur.down()

        def rotate(self, angle, direction):
            if direction == 'R':
                self.tur.right(angle)
            if direction == 'L':
                self.tur.left(angle)

        def move(self, dis, draw = False, heading = None):
            if heading != None:
                self.tur.seth(heading)

            if draw:
                self.tur.down()
            else:
                self.tur.up()

            self.tur.forward(dis)

        def move_right(self, dis):
            self.move(dis, False, 0)

        def move_up(self, dis):
            self.move(dis, False, 90)

        def move_left(self, dis):
            self.move(dis, False, 180)        

        def move_down(self, dis):
            self.move(dis, False, 270)

    class artControl(motionControl):
        def __init__(self, Tur):
            self.tur = Tur

        def circle(self, r):
            self.tur.down()
            self.tur.seth(0)
            self.tur.circle(r)

        def semi_circle(self, r, extend):
            self.tur.down()
            self.tur.circle(r, extend)

        def move_circle(self, r):
            self.tur.down()
            self.move(r, False, 270)
            self.circle(r)

        def oval(self, r):
            for loop in range(2):
                self.semi_circle(r, 90)
                self.semi_circle(r/2, 90)

        def line(self, dis):
            self.move(dis, True)

        def line_right(self, dis):
            self.move(dis, True, 0)

        def line_left(self, dis):
            self.move(dis, True, 180)

        def line_up(self, dis):
            self.move(dis, True, 90)

        def line_down(self, dis):
            self.move(dis, True, 270)

        def outline_color(self, Color):
            self.tur.color(Color,'white')
            self.tur.begin_fill()

        def fill_color(self, Color):
            self.tur.fillcolor(Color)
            self.tur.begin_fill()

        def end_fill(self):
            self.tur.end_fill()
            self.tur.color('black')
            
