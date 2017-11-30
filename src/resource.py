# resource.py

from QuantityError import QuantityError

class Resource:
    CONST_LIFE_RESOURCE = 2
    CONST_DIFF = 3

    def checkquantity(self):
        try:
            if(self.quantity < 0):
                raise QuantityError
        except QuantityError:
            self.quantity = 0

    def setquantity(self, num):
        raise NotImplementedError

    def getquantity(self):
        raise NotImplementedError

    def increment(self):
        raise NotImplementedError

    def increments(self, num):
        raise NotImplementedError

    def decrement(self):
        raise NotImplementedError

    def decrements(self, num):
        raise NotImplementedError