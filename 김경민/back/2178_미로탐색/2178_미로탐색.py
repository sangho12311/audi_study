
from collections import deque

import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1:
                q.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1

    return miro[N-1][M-1]


print(bfs(0, 0))
