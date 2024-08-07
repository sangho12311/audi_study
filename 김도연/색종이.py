arr = [[0]*100 for _ in range(100)]
count =0 
T = int(input())
for i in range(1,T+1):

    H,W = map(int,input().split())
    for a in range(H,H+11):
        for b in range(W,W+11):
            if 0<=a<100 and 0<=b<100:
                arr[a][b] = 1


# Count the number of cells that are covered
for row in arr:
    for cell in row:
        if cell == 1:
            count += 1

# Print the total count of covered cells
print(count)
