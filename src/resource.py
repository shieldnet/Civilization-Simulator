# resource.py

class Resource:
    CONST_LIFE_RESOURCE = 2
    CONST_DIFF = 3
    _importance = 100
    _is_lif_rsc = False
    
    def checkquantity(self):
        if(self.quantity < 0):
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
    
    def is_life_rsc(self):
        return self._is_lif_rsc