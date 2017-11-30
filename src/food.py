# food.py

from resource import Resource

class Food(Resource):
    def __init__(self, num):
        self.quantity = num

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
        self.checkquantity()

    def decrements(self, num):
        self.quantity -= num
        self.checkquantity()