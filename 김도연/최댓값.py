N = 9

arr = [list(map(int,input().split())) for _ in range(N)]
max_v = 0 # 초기값 설정
max_idx = (0,0) # max_v 좌표설정

for a in range(N):
    for b in range(N):
        if arr[a][b] > max_v:
            max_v = arr[a][b]
            max_idx = (a,b)

print(max_v)
print(max_idx[0]+1,max_idx[1]+1) 
