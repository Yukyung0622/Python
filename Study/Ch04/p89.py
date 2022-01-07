#리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y    #new object
print(z)    #[1, 2, 3, 4, 1.5, 2.5]

#리스트 확장
x.extend(y)  #x확장
print(x)    #[1, 2, 3, 4, 1.5, 2.5]

#리스트 추가
x.append(y) #x추가
print(x)    #[1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

#리스트 두 배 확장
lst = [1, 2, 3, 4]  #list생성
result = lst * 2  #각 원소 연산 안됨
print(result)     #[1, 2, 3, 4, 1, 2, 3, 4]