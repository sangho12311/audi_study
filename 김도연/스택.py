T = int(input())
stack=[]
for t in range(T):
    word = input()
    if 'push' in word:
        _ ,i = word.split() # 띄어쓰기 기준 i출력
        stack.append(int(i))
        
    elif 'top' in word:
        if stack: # stack이 차있으면,
            print(stack[-1])
        else:
            print(-1)
    
    elif 'empty' in word:
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif 'pop' in word:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif 'size' in word:
        print(len(stack))
    
    
