def solution(num):
    answer = ''
    if num % 2 == 0:
    # 입력받은 num을 2로 나눴을 때 나머지가 0인 경우
        answer = "Even"
        # answer에 "Even" 대입
    else:
    # 입력받은 num을 2로 나눴을 때 나머지가 0이 아닌 경우
        answer = "Odd"
        # answer에 "Odd" 대입
    return answer
