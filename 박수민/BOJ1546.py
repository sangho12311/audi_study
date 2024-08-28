import sys
input = sys.stdin.read

def main():
    # 입력 데이터 읽어오기
    data = input().strip().split()
    
    # 첫 번째 데이터는 배열의 크기
    n = int(data[0])
    
    # 배열의 나머지 데이터는 수의 리스트
    nums = list(map(int, data[1:n+1]))
    
    # 최대값과 총합을 계산
    max_val = max(nums)
    total_sum = sum(nums)
    
    # 결과 계산
    result = (total_sum / max_val * 100) / n
    
    # 결과 출력
    print(result)

if __name__ == "__main__":
    main()
