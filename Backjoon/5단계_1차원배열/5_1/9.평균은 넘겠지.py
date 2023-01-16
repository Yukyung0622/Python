n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for j in nums[1:]:
        if j > avg:
            cnt += 1
    per = (cnt/nums[0])*100
    print('%.3f'%per+'%')