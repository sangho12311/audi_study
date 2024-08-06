import math

N = int(input())
size = list(map(int,input().split()))
T,P = map(int,input().split())

T_order = 0
for i in size :
    T_order += math.ceil(i/T)
    # 필요 티셔츠 수 올림하여 계산

print(T_order)
print(N//P,N%P)
