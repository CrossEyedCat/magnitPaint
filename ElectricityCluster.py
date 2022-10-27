import numpy as np


class ElectricityCluster:
    collection = []
    size = 0

    def __init__(self):
        self.collection = []

    def add_electricity(self, elec):
        self.size = self.size + 1
        self.collection.append(elec)

    def get_cluster(self):
        return self.collection
