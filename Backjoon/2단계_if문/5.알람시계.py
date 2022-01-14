H,M = map(int,input().split())

if M >= 45:
    print(H,M-45)
elif M<45 and 0<H:
    print(H-1,M+15)
else:
    print(23,M+15)