while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
        
        
"""
오류처리를 위한 try, except문
try : 
    ...
except[발생 오류 [as 오류 메세지 변수]]
    ...
<try 블록 수행 중에 오류가 발생하면 except블록이 수행된다.
하지만 try 블록에서 오류가 발생하지 않는다면 except는 수행되지 않는다.>
"""