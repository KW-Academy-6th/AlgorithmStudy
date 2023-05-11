def solution(n):
    answer = 0
    for i in str(n):
    # 문자열 n을 자릿수만큼 반복
        answer += int(i)
        # 각 문자를 int 값으로 변환해 answer에 더함
    return answer
