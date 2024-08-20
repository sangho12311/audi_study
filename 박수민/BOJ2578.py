# 필요한 라이브러리 import
import sys
input = sys.stdin.read

def main():
    # 입력을 한 번에 읽어오기
    data = input().strip().split()
    
    # 5x5 빙고판 초기화
    bingo = []
    index = 0
    for i in range(5):
        bingo.append([int(data[index + j]) for j in range(5)])
        index += 5

    # 5x5 체크판 초기화
    check = [[0] * 5 for _ in range(5)]
    
    # 빙고 번호 입력 및 체크
    answer = 0
    for i in range(1, 26):
        num = int(data[index])
        index += 1
        
        # 번호를 빙고판에서 찾아 체크판 업데이트
        for j in range(5):
            for k in range(5):
                if bingo[j][k] == num:
                    check[j][k] = 1

        # 행 체크
        count = 0
        for j in range(5):
            if all(check[j][k] == 1 for k in range(5)):
                count += 1

        # 열 체크
        for j in range(5):
            if all(check[k][j] == 1 for k in range(5)):
                count += 1

        # 대각선 체크 (왼쪽 위에서 오른쪽 아래로)
        if all(check[j][j] == 1 for j in range(5)):
            count += 1

        # 대각선 체크 (오른쪽 위에서 왼쪽 아래로)
        if all(check[j][4 - j] == 1 for j in range(5)):
            count += 1

        # 3개 이상의 빙고가 있을 때, 현재 빙고 호출 번호를 저장
        if count >= 3 and answer == 0:
            answer = i

    # 결과 출력
    print(answer)

if __name__ == "__main__":
    main()
