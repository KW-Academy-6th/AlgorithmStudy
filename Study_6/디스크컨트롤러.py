import heapq

def solution(jobs):
    count = 0  # 작동 중 현재 시간
    waitHeap = []  # 작업이 대기할 최소 힙
    idx = 0  # 현재 실행 중인 job의 번호 (0부터 jobs의 길이 -1 까지)
    totalTime = 0  # 총 응답 시간

    jobs.sort()  # job의 요청 시점이 빠른 순으로 정렬
    lenJobs = len(jobs)  # jobs의 길이

    # 작업 처리를 위한 반복문
    while idx != lenJobs or waitHeap:
        # 현재 시점(count)에서 요청된 작업들을 대기 힙에 추가
        while idx != lenJobs and jobs[idx][0] <= count:
            heapq.heappush(waitHeap, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if waitHeap:  # 대기 힙에 작업이 있는 경우
            workFlag = 1
            duration, requestTime = heapq.heappop(waitHeap)
            count += duration
            totalTime += (count - requestTime)
        else:  # 대기 힙이 비어있는 경우
            count += 1
                
    return totalTime // lenJobs  # 평균 응답 시간 계산
