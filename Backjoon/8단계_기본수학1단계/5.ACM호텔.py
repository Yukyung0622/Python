t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())  # h=각 호텔의 층 수, w=각 층의 방 수, n=몇
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')