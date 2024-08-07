import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
K = int(input())

di = [-1, 1, 1, -1]
dj = [1, 1, -1, -1]

max_value = 0
for i in range(N):
    for j in range(N):
        S=0
        for e in range(len(di)):
            for k in range(1, K+1):
                ni = i + di[e]*k
                nj = j + dj[e]*k 
                if 0<= ni < N and 0<= nj <N :
                    S += arr[ni][nj]
            if max_value < S:
                max_value = S
print(f'{max_value}')



