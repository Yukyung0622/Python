numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers))+1)


"""
9개의 숫자를 입력 받으면 입력받은 수 중 가장 큰 숫자의 값과 순서를 출력하는 문제
입력받은 숫자로 리스트를 먼저 생성하고 가장 큰 숫자는 max함수를 사용해서 찾음
가장 큰 값이 몇번째 순서인지는 index함수를 이용해서 찾음
index는 함수는 0번째부터 시작하기 때문에 1를 더해준다. 
"""