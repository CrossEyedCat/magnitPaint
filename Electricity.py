import math

class Electricity:
    x = 0
    y = 0
    clockwise = 0
    def __init__(self, x, y, clockwise):
        self.x = x
        self.y = y
        self.clockwise = clockwise

    def get_vector_angle(self, vector_x, vector_y):
        if self.clockwise==1:
            angle = math.atan((vector_y - self.y) / (vector_x - self.x)) + math.pi / 2
            if (vector_x - self.x<=0):
                angle = angle + math.pi
            return angle
        angle = math.atan((vector_y - self.y) / (vector_x - self.x)) - math.pi / 2
        if (vector_x - self.x <= 0):
            angle = angle + math.pi
        return angle

    def get_clockwise(self):
        return self.clockwise

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vector_length(self, vector_x, vector_y):
        len = 500/math.sqrt(((self.x-vector_x)*(self.x-vector_x)+(self.y-vector_y)*(self.y-vector_y))/5)
        if len > 25 or math.sqrt(((self.x-vector_x)*(self.x-vector_x)+(self.y-vector_y)*(self.y-vector_y)))<=20:
            len = 0
        return len

