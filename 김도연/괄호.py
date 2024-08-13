T = int(input())
tc = [list(input()) for _ in range(T)]


for i in range(len(tc)):
    stack = []
    isTrue = True
    for j in range(len(tc[i])):
        if tc[i][j] == '(':
            stack.append(tc[i][j])
        else :
            if len(stack) == 0:
                isTrue = False
                print('NO')
                break
            elif len(stack) != 0:
                stack.pop()
    if isTrue == False :
        continue
    if len(stack) != 0:
        print('NO')
    elif len(stack) == 0:
        print('YES')




