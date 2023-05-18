from collections import deque#앞에가 먼저 나가야 하기 때문에 큐 활용해서 풀어봄

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    hap = 0 #다리위에 올라가있는 차의 무게  sum(dari)로 하면 속도가 느려 통과가 안됨.... 따라서 직접계산필요
    dari = deque([0] * bridge_length)#앞뒤로 추가하거나 삭제해야하기 때문에 큐 사용
    truck_weights = deque(truck_weights) #앞에가 먼저 나가야 하기 때문에 큐 활용해서 풀어봄

    while truck_weights or hap > 0:
        hap -= dari.popleft()#하나 뺐으니까  dari 길이
            #대기트럭이 존재하고        다리위에 있는 차무게가 한계무게보다 작으면
        if len(truck_weights)>0 and hap + truck_weights[0] <= weight:#차가 추가 된 경우
            truck = truck_weights.popleft()#제일 앞에 있는 애 하나 뽑아서 
            hap += truck#무게추가하고
            dari.append(truck)#다리위에 태우기
        else:#차가 추가 되지 못한 경우 
            #하나 뺐으니까  dari 길이를 유지하기 위해 맨 뒤에 추가
            dari.append(0)
        cnt += 1

    return cnt