import math


class Electricity:
    def __init__(self, x, y, clockwise):
        self.x = x
        self.y = y
        self.clockwise = clockwise

    def get_vector_angle(self, vector_x, vector_y):
        x = vector_x - self.x
        y = vector_y - self.y
        try:
            angle = math.atan(y / x)
        except:
            angle = 0
        if x <= 0:
            angle += math.pi
        if self.clockwise:
            angle += math.pi / 2
            return angle
        angle -= math.pi / 2
        return angle

    def get_clockwise(self):
        return self.clockwise

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_vector_length(self, vector_x, vector_y):
        x = self.x - vector_x
        y = self.y - vector_y
        num = x * x + y * y
        length = 100000 / num

        if length > 625.0 or num <= 400.0:
            return 0
        return math.sqrt(length)
