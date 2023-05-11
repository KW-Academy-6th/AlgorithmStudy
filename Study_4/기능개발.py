def solution(progresses, speeds):
    answer = []
    cnt = 0
    day = 0
    while len(progresses) > 0:                          # progresses에 값이 남아있지 않을 때까지 반복
        if (progresses[0] + speeds[0] * day) >= 100:    # 첫 번째 칸의 작업이 끝난 경우
            progresses.pop(0)
            speeds.pop(0)                               # progresses와 speeds의 첫 번째 칸 값을 제거
            cnt += 1                                    # 작업이 하나 끝났으므로 cnt+1
        else:
            if cnt > 0:                                 # cnt가 0보다 큰 경우(지난 day 동안 완료된 작업이 있음)
                answer.append(cnt)                      # answer에 완료된 작업 개수 넣기
                cnt = 0                                 # cnt 초기화
            day += 1                                    # 하루가 지나감 day+1
    answer.append(cnt)                                  # while문을 벗어난 이후 마지막 cnt를 answer에 넣기
    return answer
