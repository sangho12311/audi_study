N = int(input())
score = list(map(int,input().split()))
max_v = max(score) # 점수 중 최댓값
new_score = [] #거짓점수

for num in score:
    new_score.append((num/max_v)*100)

result = sum(new_score)/N
print(f'{result:.3f}')

