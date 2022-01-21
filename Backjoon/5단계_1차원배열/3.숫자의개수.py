a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))

"""
a,b,c를 각각 입력을 받고 result 변수를 설정해서 a,b,c를 곱한 값을 
문자열(str)로 변환후 list[]로 묶는다.

result = list("17037300")
result = [1, 7, 0, 3, 7, 9, 0, 0]
" "안에 들어있는 문자열(str)은 list를 사용해서 리스트로 변형해주면
0부터 각각의 index로 저장된다.

for문을 이용해서 i = 0~9까지 문자열(str)만 가능한 함수인 count를 사용해서
i를 str(i)를 통해서 문자열로 바꿔준 뒤 count를 이용해서 
result 리스트[]안에 그 수가 있는지 확인한 뒤 , 그 수 만큼을 print하면 끝!

간단한 문제이지만
정수(int)끼리 곱한 값을 문자열(str)로 바꾼뒤 list함수를 이용해서 리스트화 시키고,
count함수를 사용하기 위해서 정수(int)가 아닌 문자열(str)로 바꾼뒤 
출력해야된다.
"""