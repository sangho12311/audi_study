T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0
            for a in range(M):
                for b in range(M):
                    sum_v += arr[i+a][j+b]
            
            max_v = max(max_v,sum_v)
print(f'#{t} {max_v}')

