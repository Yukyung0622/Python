"""
날짜 : 2022/02/11
이름 : 김유경
내용 : 코딩테스트 구현 실습
"""

n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):

            #정수로 받아서 글자로 계산
            time = str(h) + str(m) + str(s)
            #3이 h, m, s에 포함되어 있으면
            if '3' in time:
                count +=1


print(count)