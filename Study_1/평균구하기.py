def solution(arr):
    answer = 0
    hap = 0     # 배열 값들을 전부 더한 값을 저장할 변수
    for i in arr:   # 배열 값의 개수만큼 반복
        hap += i    # 배열 값들을 hap에 더함
    answer = hap / len(arr)
    # 배열 값들을 전부 더한 hap을 배열의 길이 값으로 나눔
    return answer
