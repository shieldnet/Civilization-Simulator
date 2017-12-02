from firebase import firebase

firebase = firebase.FirebaseApplication('https://villiagesimulator.firebaseio.com', None)

# DB Manager
class DBManager:
    def __init__(self,civil_dic1, civil_dic2):
        self._civil_dic1 = civil_dic1
        self._civil_dic2 = civil_dic2
    
    # Initialize DB from server
    def first_get_db(self, civil_num):
        if civil_num is 1:
            return firebase.get('/Civilization1', None)
        else:
            return firebase.get('/Civilization2', None)
    
    # Update Databse to server
    def upload_db(self, ref_dic, num_of_civil):
        firebase.patch('/Civilization' + str(num_of_civil), ref_dic)
        
    def download_db(self, num_of_civil):
        return firebase.get('/Civilization' + str(num_of_civil), None)

    