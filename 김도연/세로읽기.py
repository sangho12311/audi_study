arr = [[0]*100 for _ in range(100)]

T = int(input())
for i in range(1,T+1):    
    W,H = map(int,input().split())
    for a in range(W,W+10):
        for b in range(H,H+10):
            if 0<=a<100 and 0<=b<100:
                arr[a][b] = 1

width = 0     
for x in range(100):
    for y in range(100):
        if arr[x][y]:
            width += 1
print(width)