import sys
import Person

# Civilization Class
class Civilization:
    def __init__(self):
        self.my_exchange_table = [[0 for col in range(3)] for row in range(3)]
        self.other_exchange_table = [[0 for col in range(3)] for row in range(3)]
        
        self.rsc_enum = {'food': 0, 'water': 1, 'wood': 2}
        
        self._init_rsc_table(self.my_exchange_table, -1)
        self._init_rsc_table(self.other_exchange_table, -1)
        self.degree_of_civilized = 0
        # Resource Object List
        
        # Person Object List
        self.tool_maker = Person.ToolMaker()
        self.food_maker = Person.FoodMaker()
        self.water_maker = Person.WaterMaker()

        # Communication Object
        
    
    def _init_rsc_table(self, _table, num):
        for r in range(0, 3):
            for c in range(0, 3):
                if r is c: pass
                else:
                    _table[r][c] = num
    
    def rsc_produce(self):
        pass
    
    def exchange_rsc(self):
        pass
    
    def calc_rsc_produce(self):
        pass
    
    def person_movement(self):
        pass
    
a = Civilization()

print(a.my_exchange_table)
print(a.other_exchange_table)