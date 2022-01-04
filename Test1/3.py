"""
날짜 : 2022/01/04
이름 : 김유경
내용 : 파이썬 조건문 연습문제
"""

score = int(input('점수 입력 :'))
grade = None

print('입력한 점수는 %d점이고, 등급은' % score, end='' )

if(90 <= score and score<=100 ) :
    grade ='A'
elif( 80 <=score and score < 90) :
    grade = 'B'
elif 70 <= score <80 :
    grade = 'C'
elif 60 <=score <70 :
    grade = 'D'
else:
    grade = 'F'

print('%s입니다.' % grade)