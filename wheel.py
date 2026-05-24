#==== Wheel Type Backend Logic ====#

import random

class Wheel:
    def __init__(self, wheel_name, item_names, item_weights):
        self.wheel_name = wheel_name
        self.item_names = item_names
        self.item_weights = item_weights

    def printInfo(self):
        print(self.wheel_name)
        print(self.item_names)
        print(self.item_weights)

    def spin(self):
        return random.choices(self.item_names, weights=self.item_weights, k=1)[0]
