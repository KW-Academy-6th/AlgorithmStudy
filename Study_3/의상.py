def solution(clothes):
    answer = 1
    combination = dict()                # 옷의 개수를 종류 별로 정리할 딕셔너리
    for cl in clothes:
        if cl[1] in combination:        # 옷의 종류가 key에 있는 경우
            combination[cl[1]] += 1     # 해당 value 값 +1
        else:                           # 처음 나오는 옷의 종류인 경우
            combination[cl[1]] = 1      # 해당 value 값 1로 설정

    for cnt in combination.values():
        answer *= (cnt + 1)             # 옷의 개수 + 1(착용X)

    return (answer - 1)                 # 아무것도 입지 않는 경우 제외
