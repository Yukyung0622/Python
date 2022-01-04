"""
날짜 : 2022/01/04
이름 : 김유경
내용 : 파이썬 최대공약수 연습문제
"""

sum = 0

for i in range(1,11):

    for j in range(1,1+i):
        sum += j
        print('%d' %j, end='+')

    print()

print('총합 : ', sum)