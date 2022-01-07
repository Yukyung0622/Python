person = {'name':'홍길동', 'age':'45', 'address' : '서울시'}

#요소검사
print(person['age'])
print('age'in person)

#요소 반복
for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)