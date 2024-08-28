from collections import deque
import sys
input = sys.stdin.read

def main():
    # 입력 데이터를 읽어오기
    data = input().strip().split()
    index = 0

    # 노드의 개수
    n = int(data[index])
    index += 1

    # 인접 리스트를 초기화
    nums = [[] for _ in range(n + 1)]

    # 간선 정보를 읽어 인접 리스트에 추가
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        nums[a].append(b)
        nums[b].append(a)
    
    # 결과를 저장할 리스트와 방문 여부를 기록할 리스트 초기화
    result = [0] * (n + 1)
    visited = [False] * (n + 1)

    # BFS를 위한 큐 초기화
    queue = deque([1])
    visited[1] = True
    
    # BFS 탐색
    while queue:
        temp = queue.popleft()
        for neighbor in nums[temp]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                result[neighbor] = temp

    # 2번 노드부터 n번 노드까지의 부모 노드를 출력
    for i in range(2, n + 1):
        print(result[i])

if __name__ == "__main__":
    main()
