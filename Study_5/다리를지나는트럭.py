from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truckOnBridge = deque([0] * bridge_length,maxlen=bridge_length) # 다리위의 상태 큐로 저장, 큐의 최대 길이 설정, 최대길이를 넘을시 앞의 값 삭제
    trcukWeightsQueue = deque(truck_weights) #트럭 대기열을 큐로 저장
    currentWeight = 0
    
    while trcukWeightsQueue:
        answer += 1
        currentWeight -= truckOnBridge.popleft()
        
        #다리의 무게에 여유가 있다면
        if currentWeight + trcukWeightsQueue[0] <= weight:
            trcukWeight = trcukWeightsQueue.popleft()
            truckOnBridge.append(trcukWeight)
            currentWeight += trcukWeight
        else: #다리의 무게에 여유가 없다면
            truckOnBridge.append(0)
    
    return answer + bridge_length
