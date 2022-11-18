import json


class ElectricityCluster:
    def __init__(self):
        self.collection = []

    def add_electricity(self, elect):
        self.collection.append(elect)

    def get_cluster(self):
        return self.collection

    def get_JSON(self):
        return json.loads(self.collection)
