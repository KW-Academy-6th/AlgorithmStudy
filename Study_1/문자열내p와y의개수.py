def solution(s):
    answer = True
    p, y = 0, 0     # p와 y의 개수를 저장할 변수
    for i in s:     # s의 길이만큼 반복
        if i == 'p' of i == 'P':
        # 문자열에 대문자, 소문자 p가 포함되어 있는 경우
            p += 1
            # p의 개수에 +1
        if i == 'y' or i == 'Y':
        # 문자열에 대문자, 소문자 y가 포함되어 있는 경우
            y += 1
            # y의 개수에 +1
        if p == y:
            answer = True
            # p의 개수와 y의 개수가 같은 경우 True
        elif p != y:
            answer = False
            # p의 개수와 y의 개수가 다른 경우 False
    return answer
