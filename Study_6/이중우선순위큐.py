import heapq

def solution(operations):
    minHeap = []  # 최소 힙
    maxHeap = []  # 최대 힙
    
    for operation in operations:
        op, num = operation.split()  # 명령어와 숫자 분리
        num = int(num)
        
        if op == 'I':  # 삽입 
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, -num)
        elif op == 'D':  # 삭제
            if not minHeap:  # 힙이 비어있는 경우 무시
                continue
            if num == 1:  # 최대값 삭제
                maxVal = heapq.heappop(maxHeap)
                minHeap.remove(-maxVal)
            elif num == -1:  # 최소값 삭제
                minVal = heapq.heappop(minHeap)
                maxHeap.remove(-minVal)
    
    if not minHeap:  # 힙이 비어있는 경우
        return [0, 0]
    else:  # 힙이 비어있지 않은 경우
        return [-heapq.heappop(maxHeap), heapq.heappop(minHeap)]
