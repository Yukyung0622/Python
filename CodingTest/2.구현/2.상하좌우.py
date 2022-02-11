"""
날짜 : 2022/02/11
이름 : 김유경
내용 : 코딩테스트 - 상하좌우
"""

n = int(input())
x,y =1,1
plans = input().split()

type = ['L','R','U','D']

for i in range(len(plans)):
    if plans[i] == type[0]:
        if y -1 == 0:
            continue
        else:
            y = y-1
    if plans[i] == type[1]:
        if y +1 == n+1:
            continue
        else:
            y = y+1
    if plans[i] == type[2]:
        if x-1 == 0:
            continue
        else:
            x = x-1
    if plans[i] == type[3]:
        if x +1 == n+1:
            continue
        else:
            x = x+1



print(x,y)