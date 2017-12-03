#import DB_Initialize
from civilization import Civilization
import time
civil1 = Civilization()


def check_defeating():
    if civil1.get_info_dic(1)['Civil1_Food'] is 0 and civil1.get_info_dic(1)['Civil1_Water'] is 0:
        print("Civil 1 is Lost")
        return 1
    elif civil1.get_info_dic(2)['Civil2_Food'] is 0 and civil1.get_info_dic(2)['Civil2_Water'] is 0:
        print("Civil 2 is Lost")
        return 1
    return 0



if __name__ == '__main__':
    i=0
    while(i!=30):
        
        civil1.set_first_info(1)
        civil1.set_first_info(2)
        
        civil1.set_rsc_importance()
        civil1.change_ratio_of_maker()
        
        civil1.rsc_produce()
        civil1.rsc_comsume()
        civil1.person_movement()
        civil1.update_info_dic(1)

        if check_defeating() is 1:
            break
        
        civil1.get_db_manager().upload_db(civil1.get_info_dic(1), 1)
        
        print(civil1.get_info_dic(1))
        print(civil1.get_info_dic(2))
        time.sleep(1)