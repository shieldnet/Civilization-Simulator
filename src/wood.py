# wood.py

import resource

class Wood(resource.Resource):
    def __init__(self, num):
        self.quantity = num

    def setquantity(self, num):
        self.quantity = num

    def getquantity(self):
        return self.quantity

    def consume(self, num):
        self.quantity -= num