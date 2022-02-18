"""
날짜 : 2022/02/18
이름 : 김유경
내용 : 코딩테스트 선택정렬 실습
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i+1, len(array)):

        if array[i] > array[j]:
            #swap - 위치 교환
            tmp = array[i]
            array[i] = array[j]
            array[j]=tmp
    #print(array) #각라운드 별로 어떻게 위치되는지 보려면!

print(array)