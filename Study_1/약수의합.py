def solution(n):
    answer = 0
    for i in range(1, n+1, 1):  # 1부터 n까지 반복
        if n % i == 0:
        # 입력받은 n을 i(1~n)으로 나눴을 때 나머지가 0인 경우
            answer += i
    return answer
