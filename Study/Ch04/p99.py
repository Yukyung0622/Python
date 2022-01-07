#dict 생성 방법
dic = dict(key1 = 100, key2 = 200, key3=300)
print(dic)

#dict 생성방법2
person = {'name':'홍길동', 'age':'45', 'address' : '서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

#원소 수정, 삭제, 추가
#dict 원소 수정
person['age'] = 45
print(person)

#dict 원소 삭제
del person['address']
print(person)

#dict 원소 추가
person['pay'] = 350
print(person)