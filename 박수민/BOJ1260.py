from collections import deque

def dfs(graph, visited, node):
    # 현재 노드를 방문 처리하고 출력
    print(node, end=' ')
    visited[node] = True
    
    # 현재 노드의 인접 노드들에 대해 DFS 호출
    for neighbor in sorted(graph[node]):
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    
    # 큐가 비어있지 않으면 계속 반복
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        # 현재 노드의 인접 노드들에 대해 BFS 처리
        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 그래프의 노드 수, 간선 수, 시작 노드 읽기
    n = int(data[0])
    m = int(data[1])
    v = int(data[2])
    
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    
    index = 3
    for _ in range(m):
        s = int(data[index])
        e = int(data[index + 1])
        index += 2
        graph[s].append(e)
        graph[e].append(s)
    
    # 각 노드의 인접 리스트를 정렬
    for i in range(1, n + 1):
        graph[i].sort()
    
    # DFS 호출
    visited = [False] * (n + 1)
    dfs(graph, visited, v)
    print()  # 줄 바꿈
    
    # BFS 호출
    visited = [False] * (n + 1)
    bfs(graph, visited, v)

if __name__ == "__main__":
    main()
