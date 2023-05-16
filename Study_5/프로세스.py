from collections import deque

def solution(priorities, location):
    answer = 0
    q_p = deque(priorities)
    while q_p:                                  # 실행해야하는 프로세스가 존재하면 계속적으로 반복
        max_p = max(q_p)                        # 현재 대기열에서 가장 우선순위가 높은 프로세스
        len_p = len(q_p)                        # 현재 대기열에 있는 프로세스 개수
        first = q_p.popleft()                   # 프로세스 하나 빼기
        if first != max_p:                      # pop한 프로세스가 우선순위 max가 아닌 경우
            q_p.append(first)                   # queue 안으로 다시 append
            location = location % len_p - 1     # 모든 프로세스가 이동했으므로 location 조정
        else:
            answer += 1                         # 실행했으므로 answer +1
            if location == 0:                   # 실행된 프로세스가 주어진 프로세스인 경우
                break                           # break
            else:                               # 실행된 프로세스가 주어진 프로세스가 아닌 경우
                location = location % len_p - 1 # location 조정
    return answer
