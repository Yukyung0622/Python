t = int(input())

for _ in range(t):
    ox = input()
    score = 0
    cnt = 0

    for i in range(len(ox)):
        if ox[i] == "O":
            cnt += 1
            score += cnt
        elif ox[i] == "X":
            cnt = 0
    print(score)
    


"""
변수 t를 설정해서 테스트 케이스를 입력받고
for문으로 테스트 케이스의 수만큼 반복을 해준다.

for문 안에서 변수 ox를 설정해서 OX를 입력받고
최종 출력될 score 변수와 테스트 케이스 마다 O의 수를 count할 변수를 만들어서
0으로 초기화 시켜놓는다.

그리고 다시 for문을 만들어서 ox에 입력받은 수만큼 반복을 해주며
if문으로 만약 ox(문자열 기본적으로 리스트)리스트에 "O"가 있다면
cnt를 1 더해주고 score에 cnt만큼을 더해줘서 누락시킨다.

그리고 "X"일 경우 (elif of else) cnt를 다시 0으로 초기화시켜줘서
그 다음 "O"를 맞이 할때 다시 1부터 cnt를 셀 수 있도록 한다.

이렇게 해서 cnt가 누적된 score를 출력해주면 끝

"""