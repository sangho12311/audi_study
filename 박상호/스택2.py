import sys

input = sys.stdin.read

# 전체 입력을 한 번에 받아옴
data = input().splitlines()
T = int(data[0])

stack = []

# 출력 결과를 담을 리스트
output = []

for i in range(1, T + 1):
    cod = list(map(int, data[i].split()))

    if cod[0] == 1:
        stack.append(cod[1])

    elif cod[0] == 2:
        if stack:
            output.append(stack.pop())
        else:
            output.append(-1)

    elif cod[0] == 3:
        output.append(len(stack))

    elif cod[0] == 4:
        if stack:
            output.append(0)
        else:
            output.append(1)

    elif cod[0] == 5:
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)

# 결과 출력
sys.stdout.write("\n".join(map(str, output)) + "\n")