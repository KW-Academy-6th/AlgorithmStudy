import heapq

def solution(scoville, K):
    heapq.heapify(scoville) #scoville을 값으로 가진 MinHeap생성
    answer = 0

    while scoville[0] < K: #가장 작은 스코빌 지수가 K 값보다 작은경우 반복
        if len(scoville) < 2: #모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
        #스코빌 지수가 가장 낮은 두 음식을 섞어 다시 힙에 삽입, 섞은 횟수 1 증가
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1

    return answer
