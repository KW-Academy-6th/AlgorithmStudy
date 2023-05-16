from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0              # 지나간 초를 기록할 변수
    in_bridge = deque([0 for _ in range(bridge_length)])
    # 다리 위 상황을 저장할 큐 (처음에는 아무도 건너지 않으므로 전부 0으로 초기화)
    while len(truck_weights) or sum(in_bridge) > 0:
    # 건널 트럭이 남아있거나, 다리 위의 무게가 0보다 큰 경우 (아직 전부 건너지 못함)
        in_bridge.popleft()                         # 가장 왼쪽 트럭 빼기
        if len(truck_weights) and sum(in_bridge) + truck_weights[0] <= weight:
        # 건널 트럭이 남아있고, 다음 트럭이 다리 위로 올라와도 무게 제한에 걸리지 않는 경우
            in_bridge.append(truck_weights[0])      # 다음 트럭 다리 위로 추가
            truck_weights.pop(0)                    # 트럭 목록에서는 빼기
        else:       # 건널 트럭이 없거나, 다음 트럭이 올라오면 무게 초과인 경우
            in_bridge.append(0)                     # 다리 위에 0 추가
        answer += 1                                 # 시간 기록
    return answer
