cre = 0
sum = 0
sum_result=0
for _ in range(20):
    arr = input().split()
    if arr[2] != 'P':
        if arr[2] == 'A+':
            sum = 4.5 * float(arr[1])
        elif arr[2] == 'A0':
            sum = 4.0 * float(arr[1])
        elif arr[2] == 'B+':
            sum = 3.5 * float(arr[1])
        elif arr[2] == 'B0':
            sum = 3.0 * float(arr[1])
        elif arr[2] == 'C+':
            sum = 2.5 * float(arr[1])
        elif arr[2] == 'C0':
            sum = 2.0 * float(arr[1])
        elif arr[2] == 'D+':
            sum = 1.5 * float(arr[1])
        elif arr[2] == 'D0':
            sum = 1.0 * float(arr[1])
        elif arr[2] == 'F':
            sum = 0.0 * float(arr[1])
        cre += float(arr[1])
        sum_result += sum
print(round(sum_result/cre,6))