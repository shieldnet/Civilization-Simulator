# water.py

import resource

class Water(resource.Resource):
    def __init__(self, num):
        self.quantity = num

    def setquantity(self, num):
        self.quantity = num

    def getquantity(self):
        return self.quantity

    def consume(self, num):
        self.quantity -= num

"""
r1 = Water(500)
print(r1.CONST_TO_SURVIVE)
print(r1.getquantity())
r1.consume(100)
print(r1.getquantity())
"""