#원소가 한개인 경우
t = (10, )
print(t)

#원소가 여러 개인 경우
t2 = {1, 2, 3, 4, 5, 3}
print(t2)

#튜플 색인
t3 = (1, 2, 3, 4, 5, 6, 7)
print(t3[0], t3[1:4], t3[-1])

#수정불가
#t2[0] = 10 #error

#요소반복
for i in t2 :
    print(i, end= ' ')
    
#요소검사
if 6 in t2:
    print('6 있음')
else:
    print("6 없음")