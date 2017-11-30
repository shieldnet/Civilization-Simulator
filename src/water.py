# water.py

import resource
from resource import Resource

class Water(Resource):
    def __init__(self, num):
        self.quantity = num
        self._is_lif_rsc = True

    def setquantity(self, num):
        self.quantity = num

    def getquantity(self):
        return self.quantity

    def increment(self):
        self.quantity += self.CONST_DIFF

    def increments(self, num):
        self.quantity += num

    def decrement(self):
        self.quantity -= self.CONST_DIFF

    def decrements(self, num):
        self.quantity -= num