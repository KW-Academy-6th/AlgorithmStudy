def solution(x, n):
    answer = []
    for i in range(1, n+1, 1):  # 1부터 n까지 반복
        answer.append(x*i)
        # 주어진 x 값에 i를 곱한 값을 answer list에 추가
    return answer
