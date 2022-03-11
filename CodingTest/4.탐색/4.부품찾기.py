"""
날짜 : 2022/03/11
이름 : 김유경
내용 : 코딩테스트 - 부품찾기
"""


#이진 탐색 소스코드 구현(반복문)
def binary_search(dataset, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        #찾은 경우 중간점 인덱스 변환
        if dataset[mid] == target:
            return mid
        
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif dataset[mid] > target:
            end = mid - 1

        #중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
       else:
            start = mid + 1
    return None

#N(가게의 부품 개수)입력
n = int(input())

#가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
dataset = list(map(int, input().split()))

#M(손님이 확인 요청한 부품 개수) 입력
m = int(input())

#손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
ms = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in ms:
    
    #해당 부품이 존재하는지 확인
    result = binary_search(dataset, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')