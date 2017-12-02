#import DB_Initialize
from civilization import Civilization

civil1 = Civilization()

if __name__ == '__main__':
    civil1.set_first_info(1)
    print(civil1.get_info_dic(1))
    
    civil1.set_first_info(2)
    print(civil1.get_info_dic(2))
    
    civil1.rsc_produce()
    civil1.print_rsc_quantity()
    civil1.rsc_comsume()
    civil1.print_rsc_quantity()
    
    civil1.update_info_dic(1)
    civil1.get_db_manager().upload_db(civil1.get_info_dic(1), 1)

    civil1.set_first_info(1)
    print(civil1.get_info_dic(1))