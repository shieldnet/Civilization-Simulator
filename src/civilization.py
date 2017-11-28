import sys
import json

# Import Person Class
from FoodMaker import FoodMaker
from ToolMaker import ToolMaker
from WaterMaker import WaterMaker

# Import Resource Class
from food import Food
from water import Water
from wood import Wood


# Civilization Class
class Civilization:
    # const
    _NUMBER_OF_RSC = 2
    
    def __init__(self):
        self._my_exchange_table = \
            [[0 for col in range(self._NUMBER_OF_RSC + 1)] for row in range(self._NUMBER_OF_RSC + 1)]
        self._other_exchange_table = \
            [[0 for col in range(self._NUMBER_OF_RSC + 1)] for row in range(self._NUMBER_OF_RSC + 1)]
        
        self._rsc_enum = {'food': 0, 'water': 1, 'wood': 2}
        
        # Information of Civilization
        self._total_population = 0
        self._total_tools = 0
        
        
        # Initialize it
        self._init_rsc_table(self._my_exchange_table, -1)
        self._init_rsc_table(self._other_exchange_table, -1)
        
        self._degree_of_civilized = 0
        
        # Resource Object List
        self._food = Food(0)
        self._water = Water(0)
        self._wood = Wood(0)
        
        # Person Object Lists
        self._tool_maker = ToolMaker("ToolMaker")
        self._food_maker = FoodMaker("FoodMaker")
        self._water_maker = WaterMaker("WaterMaker")
        
        # Communication Object
    
    def _init_rsc_table(self, _table, num):
        for r in range(0, self._NUMBER_OF_RSC + 1):
            for c in range(0, self._NUMBER_OF_RSC + 1):
                if r is c:
                    pass
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
    
    def set_rsc_importance_(self, kind_of_rsc, quantity):
        pass
        # Importance of each Resource
        # kind_of_rsc

    
a = Civilization()

print(a._my_exchange_table)
print(a._other_exchange_table)