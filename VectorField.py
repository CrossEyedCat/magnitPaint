from MagneticVector import *


class VectorField:
    collection = []
    size = 0

    def __init__(self):
        for i in range(20):
            for l in range(20):
                vec = MagnetiсVector(i * 25, l * 25, 1, 0)
                self.size = self.size + 1
                self.collection.append(vec)

    def get_VectorField(self):
        return self.collection
