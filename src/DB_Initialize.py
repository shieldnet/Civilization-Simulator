from firebase import firebase

firebase = firebase.FirebaseApplication('https://villiagesimulator.firebaseio.com', None)

civil1_dic = {
            'Civil1_NumPeople': 500,
            'Civil1_Food': 2500,
            'Civil1_Water': 2500,
            'Civil1_DegOfCivilized': 1000,
        }

civil2_dic = {
            'Civil2_NumPeople': 500,
            'Civil2_Food': 10000,
            'Civil2_Water': 10000,
            'Civil2_DegOfCivilized': 1000,
        }

firebase.patch('/Civilization1', civil1_dic)
firebase.patch('/Civilization2', civil2_dic)