n = int(input())
num = n
cnt = 0

while True:
    a = num //10
    b = num%10
    c = (a+b)%10
    num = (b*10) +c

    cnt +=1
    if(num == n):
        break

print(cnt)


"""
26으로 입력했을 때 필요한 수 는
10의 자리 2
1의 자리 6

while문의 a = 2를 구하는 것은 10으로 나눈 몫
while문의 b = 6은 26으로 나눈 나머지 값
while문의 c = a+b를 하고 10으로 나눈 나머지 값

num을 n으로 선언해주고 num을 while문에 반복시킨다.
한번싸이클이 돌때 마다 count 1씩 높여준다.

원래의 n과 num이 같아진다면 break를 하고 cnt를 출력해준다.

*요약*
n과 num이 같아질때까지 while문을 돌린다.
10의 자리 수를 구하는 것은 10으로 나눈 몫, 1의 자리 수를 구하는 것은 10으로 나눈 나머지를
활용하여 필요한 숫자를 만든다.
사이클이 돌때마다 count를 1씩 높인다.
"""