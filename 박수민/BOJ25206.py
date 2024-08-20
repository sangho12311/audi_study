import sys

def main():
    input = sys.stdin.read  # 표준 입력을 읽기 위한 함수
    data = input().splitlines()  # 입력 데이터를 줄 단위로 나누어 리스트에 저장
    
    sum = 0.0  # 총 가중평균 점수
    count = 0.0  # 총 학점
    
    # 20개의 과목 정보를 처리
    for line in data:
        parts = line.split()  # 입력된 줄을 공백 기준으로 나누어 리스트로 저장
        trash = parts[0]  # 과목 이름은 무시
        score = float(parts[1])  # 학점을 실수로 변환
        grade = parts[2]  # 학점 등급
        
        # 학점 등급에 따라 가중치를 더함
        if grade == "A+":
            sum += score * 4.5
        elif grade == "A0":
            sum += score * 4.0
        elif grade == "B+":
            sum += score * 3.5
        elif grade == "B0":
            sum += score * 3.0
        elif grade == "C+":
            sum += score * 2.5
        elif grade == "C0":
            sum += score * 2.0
        elif grade == "D+":
            sum += score * 1.5
        elif grade == "D0":
            sum += score * 1.0
        elif grade == "P":
            continue  # Pass는 학점 계산에 포함하지 않음
        
        count += score  # 학점을 총 학점에 더함
    
    # 가중 평균 점수 계산 후 출력
    if count > 0:
        print(f"{sum / count:.6f}")  # 소수점 6자리까지 출력
    else:
        print("0.000000")  # 학점이 없을 경우 0으로 출력

if __name__ == "__main__":
    main()
