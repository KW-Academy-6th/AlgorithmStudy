import heapq

def solution(jobs):
    answer = 0
    time, idx = 0, 0
    length = len(jobs)
    task_heap = []
    
    # 요청 시간 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    while idx < length or task_heap:
        # 작업 대기열에서 현재 시간 전에 도착한 작업을 우선순위 큐에 추가
        while idx < length and jobs[idx][0] <= time:
            heapq.heappush(task_heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if not task_heap:
            # 작업 대기열이 비어있다면 현재 시간을 다음 작업의 시작 시간으로 설정
            time = jobs[idx][0]
        else:
            # 우선 순위 큐에서 시간이 가장 적게 걸리는 작업 선택
            task = heapq.heappop(task_heap)
            answer += time - task[1] + task[0]
            time += task[0]
    
    return answer // length

# "하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다."
# -> 배열의 인덱스가 아닌 요청 시간 기준으로 정합니다.
# -> 하드디스크가 끊임없이 작업을 처리해야 한다는 말이 아닌, 먼저 요청이 들어온 작업의 요청 시간 까지 기다린 후에 작업을 재개하는 것입니다.

# 하드디스크가 작업을 수행하지 않을 때는 시간을 세지 않습니다.
# 예) [[0,3], [10,1]] 일 때 (3 + 1) / 2 = 2 입니다. 3~10초 까지 작업을 수행하지 않으므로 시간을 세지 않습니다.
# # 따라서 중간에 시간이 붕 뜰 때는 기존의 끊임없이 작업이 이어질 수 있는 구조(예제1)와는 다른 방식으로 연산을 수행해야 합니다.
# jobs 배열을 요청시간 기준으로 오름차순으로 정렬하기