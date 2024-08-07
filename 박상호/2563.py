T=int(input())

table=[[False for _ in range(100)] for _ in range(100)]
for _ in range(T):
    R,C=map(int,input().split())
    for r in range(R,R+10):
        for c in range(C,C+10):
            if r<=100 and c<=100:
                table[r][c]=True
cnt=0               
for i in range(100):
    for j in range(100):
        if table[i][j]==True:
            cnt+=1
print(cnt)