import sys
input = sys.stdin.read

def main():
    # 입력을 한 번에 읽어오기
    data = input().strip()
    
    # 입력 문자열을 공백 기준으로 분리
    A, B, V = map(int, data.split())
    
    # (V-B) / (A-B) 계산하여 올림 처리
    count = (V - B) // (A - B)
    if (V - B) % (A - B) != 0:
        count += 1
    
    # 결과 출력
    print(count)

if __name__ == "__main__":
    main()
