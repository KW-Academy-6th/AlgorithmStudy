def solution(arr):
    answer = []
    answer.append(arr[0])               # 첫번째 숫자 list에 넣기
    compare = arr[0]                    # 비교용 변수에 저장
    for i in range(1, len(arr)):
        if compare != arr[i]:           # 이전 값과 현재 값이 다른 경우
            answer.append(arr[i])       # list에 넣기
            compare = arr[i]            # compare 변수에 현재 값 넣기
    return answer
