from firebase import firebase

firebase = firebase.FirebaseApplication('https://villiagesimulator.firebaseio.com', None)

civil1_dic = {
            'Civil1_NumPeople': 500,
            'Civil1_Food': 8000,
            'Civil1_Water': 5000,
            'Civil1_DegOfCivilized': 1000,
        }

civil2_dic = {
            'Civil2_NumPeople': 500,
            'Civil2_Food': 5000,
            'Civil2_Water': 7000,
            'Civil2_DegOfCivilized': 1000,
        }

firebase.patch('/Civilization1', civil1_dic)
firebase.patch('/Civilization2', civil2_dic)