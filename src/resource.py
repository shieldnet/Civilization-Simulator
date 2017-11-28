# resource.py

class Resource:
    CONST_LIFE_RESOURCE = 2

    def setquantity(self, num):
        raise NotImplementedError

    def getquantity(self):
        raise NotImplementedError

    def consume(self, num):
        raise NotImplementedError