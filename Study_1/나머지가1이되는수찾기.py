def solution(n):
    answer = 0
    for i in range(1, n, 1):    # 1부터 (n-1)까지 반복
        if n % i == 1:
        # n을 i(1~(n-1))로 나눈 나머지 값이 1인 경우
            answer = i
            # answer에 i 값 대입
            break
            # 나머지가 1이 되는 가장 작은 자연수가 나왔으므로 break
    return answer
