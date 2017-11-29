from firebase import firebase

firebase = firebase.FirebaseApplication('https://villiagesimulator.firebaseio.com', None)

#문서 : http://ozgur.github.io/python-firebase/
#첫번째 루틴 villiage1, villiage2 값 같이 받아옴 초깃값 다 0으로 설정 초깃값 바꿀 수 있음
# 전체 값 받아보기
vil1 = firebase.get('/villiage1', None)
# 일부 특정 키 에 해당 되는 값 받아오기
#vil1 = firebase.get('/villiage1', 'BuyCost')
vil2 = firebase.get('/villiage2', None)
print(vil1)
print(vil2)

# TODO

#해당 키에 되는거 값 Update , Post는 하지 마세요
update_vil1 = firebase.patch('/villiage1', {'BuyCost' : 3})
update_vil2 = firebase.patch('/villiage2', {'NumPeople' : 5, 'Production' : 2})

print(update_vil1)
print(update_vil2)







