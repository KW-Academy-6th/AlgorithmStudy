# from collections import deque
from heapq import heappop, heappush, heapify

def solution(scoville, K):
    cnt = 0

    # 최소힙 구조로 변환
    heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <2:
            cnt=-1
            break
        new1 = heappop(scoville)
        new2 = heappop(scoville)
        heappush(scoville, new1 + (new2 * 2))
        cnt += 1
    return cnt    

# # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)