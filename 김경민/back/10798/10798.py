# 빈 리스트를 생성
arr = []

# 5번 반복해서 입력
for _ in range(5):
    a = input()  # 
    arr.append(a)  # 입력된 문자열을 리스트에 추가

# 각 문자열을 세로로 읽어야 하므로, 최대 문자열 길이를 구함.
max_length = max(len(w) for w in arr)

# 최대 문자열 길이만큼 반복
for i in range(max_length):
    # 5개의 문자열을 순차적으로 탐색함
    for j in range(5):
        # 현재 문자열의 길이보다 i가 작은 경우에만 문자를 출력.
        if i < len(arr[j]):
            print(arr[j][i], end="")  