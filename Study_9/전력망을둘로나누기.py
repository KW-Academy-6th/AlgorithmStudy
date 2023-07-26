from collections import deque

def solution(n, wires):
    answer = 100000
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:                          # 각 노드에서 연결된 내용들 저장
        graph[a].append(b)
        graph[b].append(a)
        
    for parent, child in wires:
        visited = [False for _ in range(n+1)]   # 방문 여부
        q = deque()
        q.append(parent)                        # 끊을 선과 연결된 첫번째 노드를 queue에 추가
        result = 1                              # 시작점 방문 1
        visited[parent] = True                  # 시작점 방문
        visited[child] = True                   # 끊어진 노드는 세면 안되므로 방문 처리
        
        while q:
            node = q.popleft()                  # 연결 확인을 위해 pop
            for i in graph[node]:               # 해당 노드와 연결된 노드들 확인
                if not visited[i]:              # 방문 처리 되어있지 않는 경우
                    result += 1                 # 방문 +1
                    visited[i] = True           # 방문 처리
                    q.append(i)                 # 그 노드로부터 연결된 노드들도 검사해야 하므로 queue에 추가
        
        min_v = min(result, n-result)           # 노드 개수가 적은 쪽
        max_v = n-min_v                         # 노드 개수가 많은 쪽
        if answer > max_v - min_v:              # 두 구역의 차가 현재 계산해둔 값보다 작은 경우 update
            answer = max_v - min_v
    return answer
