import math


class Magnetic_Vector:
    x = 0
    y = 0
    length = 0
    angle = 0

    def __init__(self, x, y, length=1, angle=0):
        self.x = x
        self.y = y
        self.length = length
        self.angle = angle

    def draw(self, event):
        end_x = self.x + self.length * math.cos(self.angle)
        end_y = self.y + self.length * math.sin(self.angle)
        event.widget.create_line(self.x, self.y, end_x,
                                 end_y, fill="black")
        ug = self.angle + math.pi * 1.25
        ug2 = ug - math.pi / 2
        event.widget.create_line(end_x,
                                 end_y,
                                 end_x + self.length / 3 * math.cos(ug),
                                 end_y + self.length * math.sin(ug),
                                 fill="black")
        event.widget.create_line(end_x,
                                 end_y,
                                 end_x + self.length / 3 * math.cos(ug2),
                                 end_y + self.length * math.sin(ug2),
                                 fill="black")

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_angle(self):
        return self.angle

    def set_angle(self, ang):
        self.angle = ang
