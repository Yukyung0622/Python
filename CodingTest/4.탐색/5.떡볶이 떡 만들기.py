"""
날짜 : 2022/03/11
이름 : 김유경
내용 : 코딩테스트 - 떡볶이 떡 만들기
"""

#떡의 개수 (N)와 요청한 떡의 길이(M)을 입력
n, m =map(int, input().split())

#각 떡의 개별 높이 정보를 입력
dataset = list(map(int, input().split()))

#이진 탐색을 위한 시작점과 끝점 설정
start, end = 0, max(dataset)

#이진 탐색 수행(반복문)

while(start <= end):
    mid = (start + end) // 2
    total = 0
    
    for i in dataset:
        
        #잘랐을때의 떡볶이 양 계산
        if i > mid:
            total =total+(i-mid)
    
    #떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid -1
    
    #떡볶이 양이 충분한 경우 덜자르기 (왼쪽 부분 탐색)
    else:
        #최대한 덜잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid
        start =mid+1
print(result)