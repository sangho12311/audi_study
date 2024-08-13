import sys
input = sys.stdin.read

# 모든 입력을 한 번에 받아옴
data = input().splitlines()
T = int(data[0])  # 첫 번째 줄이 T

stack = []

for i in range(1, T + 1):
    code = data[i]
    if 'push' in code:
        _, num = code.split()
        stack.append(int(num))

    elif code == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif code == 'pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    elif code == 'size':
        print(len(stack))

    elif code == 'empty':
        if stack:
            print(0)
        else:
            print(1)