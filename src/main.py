import DB_Initialize
from civilization import Civilization

civil1 = Civilization()

if __name__ == '__main__':
    civil1.set_first_info(1)
    print(civil1.get_info_dic(1))
    
    civil1.set_first_info(2)
    print(civil1.get_info_dic(2))
