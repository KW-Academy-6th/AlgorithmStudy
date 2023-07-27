from collections import defaultdict

# DFS를 이용하여 노드의 개수를 계산하는 함수
def dfs(node, parent, graph, count):
    for i in graph[node]:
        # 자식 노드가 부모 노드인 경우 스킵하여 사이클 방지
        if i == parent:
            continue
        # 자식 노드에서 노드 개수를 재귀적으로 계산하고 더함
        count[node] += dfs(i, node, graph, count)
    return count[node]

def solution(n, wires):
    # 그래프 생성
    graph = defaultdict(list)
    # 노드 개수를 저장하는 리스트 생성
    count = [1] * (n + 1)

    # 그래프 생성 (양방향 연결)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 1번 노드를 루트로 하는 DFS를 실행하여 노드 개수를 계산
    dfs(1, 0, graph, count)

    # 초기 답을 노드 개수로 설정
    answer = n
    # 각 선분을 하나씩 제거하면서 최소 노드 개수 차이를 계산
    for a, b in wires:
        # 노드 개수의 차이를 구하고, 이전의 최소값과 비교하여 더 작은 값을 저장
        answer = min(answer, abs(n - 2 * min(count[a], count[b])))

    return answer
