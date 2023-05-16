def solution(prices):
    answer = []
    cnt = 0
    for i in range(len(prices)-1):          # 마지막 값을 제외하고 반복
        for j in range(i+1, len(prices)):   # 비교할 대상 (2~마지막)
            cnt += 1                        # 아직 가격이 떨어지지 않았으므로 +1
            if prices[i] <= prices[j]:      # 1초 뒤에 가격이 떨어지지 않은 경우
                continue                    # continue
            else:                           # 1초 뒤에 가격이 떨어진 경우
                break                       # break
        answer.append(cnt)                  # answer에 cnt 값 넣기
        cnt = 0                             # cnt 값 초기화
    answer.append(0)                        # 마지막 값의 유지시간은 무조건 0초
    return answer
