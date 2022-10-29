from MagneticVector import *


class VectorField:
    collection = []

    def __init__(self):
        for i in range(20):
            for j in range(20):
                vec = Magnetic_Vector(i * 25, j * 25)
                self.collection.append(vec)

    def get_VectorField(self):
        return self.collection
