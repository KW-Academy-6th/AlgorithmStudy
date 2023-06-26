import heapq

def solution(scoville, K):
    heapq.heapify(scoville)                 # heap
    
    count = 0                               # 음식을 섞은 횟수
    new_s = 0                               # 섞은 스코빌 값
    
    while scoville:                                                         
        min1 = heapq.heappop(scoville)      # 가장 작은 값 pop
        if min1 < K:                        # 가장 작은 값이 K보다 작은 경우
            if len(scoville) == 0:          # 값을 하나 뺀 scoville에 남은 값이 없는 경우 
                return -1                   # 뺀 값이 K보다 작기 때문에 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없다
            min2 = heapq.heappop(scoville)  # 두 번째로 작은 값 pop
            new_s = min1 + min2 * 2         # 섞은 음식 스코빌 지수 계산
            heapq.heappush(scoville, new_s) # 계산한 값 다시 push
            count += 1                      # 한번 섞었으므로 count +1
        else:                               # 가장 작은 값이 k보다 작지 않은 경우
            return count                    # 섞은 횟수 return
