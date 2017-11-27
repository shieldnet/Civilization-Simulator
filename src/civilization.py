import sys

# Civilization Class
class Civilization:
    def __init__(self):
        self.exchange_table = [[0 for col in range(3)] for row in range(3)]
        self.rsc_enum = {'food': 0, 'water': 1, 'wood': 2}
        self._init_table()
        
        pass
    
    def _init_table(self):
        for r in range(0,3):
            for c in range(0,3):
                if r is c: pass
                else:
                    self.exchange_table[r][c] = 1
    
    def rsc_produce(self):
        pass
    
    def exchange_rsc(self):
        pass
    
    def calc_rsc_produce(self):
        pass
    
    def person_movement(self):
        pass
    
a = Civilization()

print(a.exchange_table)