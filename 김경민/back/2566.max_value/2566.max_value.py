import sys
sys.stdin = open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
max_i, max_j = 0, 0
for i in range(9):
    for j in range(9):
        if max_value < arr[i][j]:
            max_value += arr[i][j]
            


