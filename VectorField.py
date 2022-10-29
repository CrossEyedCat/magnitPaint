from MagneticVector import *


class VectorField:
    collection = []

    def __init__(self):
        for i in range(50):
            for j in range(50):
                vec = Magnetic_Vector(i * 10, j * 10)
                self.collection.append(vec)

    def get_VectorField(self):
        return self.collection
