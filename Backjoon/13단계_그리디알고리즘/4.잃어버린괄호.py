expr = input().split("-")
result = sum(map(int, expr[0].split("+")))

for i in range(1, len(expr)):
    i_arr = sum(map(int, expr[i].split("+")))
    result -= i_arr

print(result)