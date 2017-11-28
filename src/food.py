# food.py

import resource


class Food(resource.Resource):
    def __init__(self, num):
        self.quantity = num

    def setquantity(self, num):
        self.quantity = num

    def getquantity(self):
        return self.quantity

    def consume(self, num):
        self.quantity -= num