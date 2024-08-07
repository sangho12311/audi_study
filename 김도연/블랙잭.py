N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_v = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_card = nums[i] + nums[j] + nums[k]
            if M >= sum_card > max_v :
                    max_v = sum_card

print(max_v)
