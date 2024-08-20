from collections import deque  # deque를 사용하기 위해 collections 모듈에서 deque를 가져옴

n = int(input())  # 사용자로부터 정수 n을 입력받음
N = deque()  # 큐 역할을 할 deque를 생성

# 1부터 n까지의 숫자를 큐에 삽입
for i in range(1, n + 1):
    N.append(i)

# 큐가 빌 때까지 반복
while N:
    temp = N.popleft()  # 큐의 앞에서 숫자를 꺼냄
    print(temp, end='')  # 꺼낸 숫자를 출력 (줄바꿈 없이)

    if not N:  # 큐가 비어있다면 반복 종료
        break
    
    temp2 = N.popleft()  # 큐의 앞에서 두 번째 숫자를 꺼냄
    N.append(temp2)  # 꺼낸 숫자를 큐의 뒤에 다시 삽입
    
    print(' ', end='')  # 숫자 사이에 공백을 출력
