name = '홍길동'
age = 35
price = 125.456

#외부 상수 인수
print('이름 : {}, 나이 : {} , data : {}'.format(name, age, price))

#format 축양형
uid = input('id input : ')
query = f'select * from memeber where uid = {uid}'
print(query)