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
        # 여기 수정중
        self._tool_maker = ToolMaker(has_tool=0, _tool=None)
        self._food_maker = FoodMaker(has_tool=0, _food=self._food)
        self._water_maker = WaterMaker(has_tool=0, _water_obj=self._water, _population=100)
        
        # Communication Object
    
    def _init_rsc_table(self, _table, num):
        for r in range(0, self._NUMBER_OF_RSC + 1):
            for c in range(0, self._NUMBER_OF_RSC + 1):
                if r is c:
                    pass
                else:
                    _table[r][c] = num
    
    def rsc_produce(self):
        self._food_maker.make_food()
        self._water_maker.make_water()
        
    def rsc_comsume(self):
        # Consume Foods
        self._food_maker.consume_food()
        self._water_maker.consume_food()
        
        # Consume Water
        self._food_maker.consume_water()
        self._water_maker.consume_water()
    
    
    def exchange_rsc(self):
        pass
    
    def calc_rsc_produce(self):
        pass
    
    def person_movement(self):
        pass
    
    def set_rsc_importance_(self, kind_of_rsc, quantity):
        if self.kind_of_rsc < 100:
            pass
        # Importance of each Resource
        # kind_of_rsc
        
    def set_first_info(self):
        pass

    
a = Civilization()

print(a._my_exchange_table)
print(a._other_exchange_table)

print(a._food.getquantity())
a._food_maker._population=100
a._food_maker.make_food()
print(a._food.getquantity())
a.rsc_comsume()
print(a._food.getquantity())