n = int(input())
test_list = list(map(int,input().split()))
max_score = max(test_list)

new_list =[]
for score in test_list:
    new_list.append(score/max_score*100)
test_avg = sum(new_list)/n
print(test_avg)

"""
과목의 숫자와 점수를 입력받으면 공식에 맞게 점수를 바꾸어 평균을 구하는 문제
새로운 점수를 구하는 공식은 입력받은 수 중 최고 점수를 분모해서
(입력받은 수 / 최고 점수 * 100)으로 계산한다.

과목수로 입력받는 수는 n에 선언하고 시험점수는 list자료형으로 test_list라는 변수에 선언한다.
새로운 점수를 구하기 위해서는 점수 중 가장 큰 점수를 찾아야 하기 때문에 test_list의
원소 중 가장 큰 값을 max 함수로 찾았다.

for문을 시작하기 전에 빈 리스트를 만든다.
리스트의 변수 이름은 new_list로 생성하였다.
이 빈 리스트에는 새로 계산된 점수를 추가하게 된다.

for문을 이용해서 입력받은 시험점수를 하나씩 꺼내면서(입력받은 점수/최고점수*100)식으로
새로운 점수를 만든다. 이렇게 새로 만든 점수는 append함수로 리스트에 추가한다.

for문이 끝나면 평균을 구한다. 새로 만든 점수로 이루어진 리스트의 요소를 sum함수로
모두 더하고서 과목수로 나눈다.
"""