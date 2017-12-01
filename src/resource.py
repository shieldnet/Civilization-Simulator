# resource.py


class Resource:
    CONST_LIFE_RESOURCE = 2
    CONST_DIFF = 3
    _importance = 0
    _is_lif_rsc = False
    
    def checkquantity(self):
        pass
    
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
