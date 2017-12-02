import sys
import random

# Import Person Class
from FoodMaker import FoodMaker
from WaterMaker import WaterMaker

# Import Resource Class
from food import Food
from water import Water

# Import Firebase Class
import DBManager
from firebase import firebase

# Civilization Class
class Civilization:
    # const
    _NUMBER_OF_RSC = 2
    CIVILNUM = 1
    
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
        
        # Person Object Lists
        # 여기 수정중
        self._food_maker = FoodMaker(has_tool=0, _food=self._food, _water=self._water, _population=0)
        self._water_maker = WaterMaker(has_tool=0, _food=self._food, _water=self._water, _population=0)
        
        # Communication Data(Dictionary)
        self._civil1_info_dic = {
            'Civil1_People': self._total_population,
            'Civil1_Food': self._food.getquantity(),
            'Civil1_Water': self._water.getquantity(),
            'Civil1_DegOfCivilized': self._degree_of_civilized,
        }
        self._civil2_info_dic = {
            'Civil2_NumPeople': 0,
            'Civil2_Food': 0,
            'Civil2_Water': 0,
            'Civil2_DegOfCivilized': 0,
         }
        
        self._db_manager = DBManager.DBManager(civil_dic1=self._civil1_info_dic, civil_dic2=self._civil2_info_dic)
    
    def _init_rsc_table(self, _table, num):
        for r in range(0, self._NUMBER_OF_RSC + 1):
            for c in range(0, self._NUMBER_OF_RSC + 1):
                if r is c:
                    pass
                else:
                    _table[r][c] = num
    
    #Produce Resource
    def rsc_produce(self):
        self._food_maker.make_food()
        self._water_maker.make_water()
     
    #Consume Resource
    def rsc_comsume(self):
        # Consume Foods
        self._food_maker.consume_food()
        self._water_maker.consume_food()
        
        # Consume Water
        self._food_maker.consume_water()
        self._water_maker.consume_water()
    
    # Exchange
    def exchange_rsc(self):
        pass
    
    # Check if is insufficient
    def is_rsc_insufficient(self, kind_of_food):
        if kind_of_food.getquantity() < self._total_population * 0.5:
            return True
        else:
            return False
    
    #ratio of resource produce
    def calc_rsc_produce(self):
        pass
    
    #amount of person movement
    def person_movement(self):
        pass
    
    def set_rsc_importance(self):
        self._set_importance(self._food)
        self._set_importance(self._water)
    
    def _set_importance(self, kind_of_rsc):
        # Importance of each Resource, Life resource amend
        importance_limit = self._total_population*0.5
        
        if self.kind_of_rsc._is_life_rsc is True:
            importance_limit *= kind_of_rsc.CONST_LIFE_RESOURCE
            
        if self.kind_of_rsc.get_quantity() < importance_limit:
            kind_of_rsc._importance += 10
        else:
            kind_of_rsc._importance = 0
        
    def set_first_info(self, num_population, num_food, num_water, deg_civilized):
        pass
    
    # Civilization 1
    def _civil1_save_data_in_dic(self):
        self._civil1_info_dic = {
            'Civil1_People': self._total_population,
            'Civil1_Food': self._food.getquantity(),
            'Civil1_Water': self._water.getquantity(),
            'Civil1_DegOfCivilized': self._degree_of_civilized,
        }
    
    # Civilization 2
    def _civil2_save_data_in_dic(self):
        # Get the data from server
        self._civil2_info_dic = {
            'Civil2_NumPeople': 0,
            'Civil2_Food': 0,
            'Civil2_Water': 0,
            'Civil2_DegOfCivilized': 0,
        }
    

    
a = Civilization()

print(a._my_exchange_table)
print(a._other_exchange_table)

print(a._food.getquantity())
a._food_maker.make_food()
print(a._food.getquantity())
a.rsc_comsume()
print(a._food.getquantity())