import math


class MagnetiсVector:
    x = 0
    y = 0
    length = 0
    angle = 0

    def __init__(self, x, y, len, angle):
        self.x = x
        self.y = y
        self.length = len
        self.angle = angle

    def draw(self, event):
        event.widget.create_line(self.x, self.y, self.x + self.length * math.cos(self.angle),
                                 self.y + self.length * math.sin(self.angle), fill="black")
        event.widget.create_line(self.x + self.length * math.cos(self.angle),
                                 self.y + self.length * math.sin(self.angle),
                                 self.x + self.length * math.cos(self.angle) + self.length / 3 * math.cos(
                                     self.angle + math.pi + math.pi / 6),
                                 self.y + self.length * math.sin(self.angle) + self.length * math.sin(
                                     self.angle + math.pi + math.pi / 4), fill="black")
        event.widget.create_line(self.x + self.length * math.cos(self.angle),
                                 self.y + self.length * math.sin(self.angle),
                                 self.x + self.length * math.cos(self.angle) + self.length / 3 * math.cos(
                                     self.angle + math.pi - math.pi / 6),
                                 self.y + self.length * math.sin(self.angle) + self.length * math.sin(
                                     self.angle + math.pi - math.pi / 4), fill="black")

    def erase(self, event):
        event.widget.create_rectangle(0, 0, 500, 500, fill="white")

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def get_length(self):
        return self.length

    def set_length(self, len):
        self.length = len

    def get_angle(self):
        return self.angle

    def set_angle(self, ang):
        self.angle = ang
