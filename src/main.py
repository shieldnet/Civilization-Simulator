#import DB_Initialize
from civilization import Civilization
import time
civil1 = Civilization()

if __name__ == '__main__':
    i=0
    while(i!=30):
        civil1.set_first_info(1)
        print(civil1.get_info_dic(1))
        
        civil1.set_first_info(2)
        
        civil1.set_rsc_importance()
        civil1.change_ratio_of_maker()
        
        civil1.rsc_produce()
        civil1.rsc_comsume()
        
        civil1.update_info_dic(1)
        civil1.get_db_manager().upload_db(civil1.get_info_dic(1), 1)
        print("importace of water"+ str(civil1._water._importance))
        print("importace of food "+ str(civil1._food._importance))
        civil1._water_maker.water_pop()
        civil1._food_maker.food_pop()
        
        print(civil1.get_info_dic(1))
        time.sleep(3)