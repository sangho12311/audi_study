import sys
input = sys.stdin.readline


T = int(input())
stack = []


for tc in range(T):
    num = input()
    if num[0] == '1':
        _ , i= num.split()
        stack.append(i)

    elif num[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif num[0]=='3':
        print(len(stack))

    elif num[0]=='4':
        if len(stack) == 0:
                print(1)
        else:
            print(0)

    elif num[0]=='5':
        if stack:
            print(stack[-1])
        else:
            print(-1)

