def solution(sizes):
    answer = 0
    max1, max2 = 0, 0                   # 가로와 세로의 최댓값을 저장할 변수
    for i in sizes:                     # 가로 길이와 세로 길이 중 더 큰 값을 0번 index로 옮김
        if i[0] <= i[1]:
            i[0], i[1] = i[1], i[0]
    for j in sizes:                     # 가로 길이 중 최대, 세로 길이 중 최대를 계산
        if max1 <= j[0]:
            max1 = j[0]
        if max2 <= j[1]:
            max2 = j[1]
    answer = max1 * max2                # 지갑의 크기 계산
    return answer
