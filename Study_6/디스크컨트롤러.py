import heapq

def solution(jobs):
    sum_job, now, count = 0, 0, 0                           # 요청 ~ 종료까지 걸린 시간, 현재 시간, 작업 수행 횟수
    num = len(jobs)                                         # 작업 개수
    wait = []                                               # heap
    jobs.sort()                                             # jobs를 요청 시간을 기준으로 sort
    while count != num:                                     # 작업을 전부 수행할 때까지 반복
        while jobs and jobs[0][0] <= now:                   # jobs가 존재하고, 요청 시간이 현재 시간보다 이전인 경우
            min_time = jobs.pop(0)                          # jobs에서 pop하고 저장 & wait에 push
            heapq.heappush(wait, [min_time[1], min_time[0]])
        if wait:                                            # wait에 값이 존재하는 경우 (바로 수행할 수 있는 작업이 존재)
            job = heapq.heappop(wait)                       # 소요 시간이 가장 작은 작업 수행
            now += job[0]                                   # 현재 시간에 소요 시간 더해서 update
            sum_job += now - job[1]                         # 요청시간 ~ 끝나는시간을 계산하여 sum_job에 더한다
            count += 1                                      # 작업 수행 횟수 +1
        else:                                               # 현재 수행할 작업이 없는 경우 현재 시간 +1
            now += 1                                        # 시간이 흘러 다음 작업이 들어오는 것을 대기
    return sum_job // num                                   # 평균 값 return
