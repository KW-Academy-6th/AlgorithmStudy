def solution(answers):
    answer = []
    cnt1, cnt2, cnt3 = 0, 0, 0              # 점수 계산 변수
    s1 = [1, 2, 3, 4, 5]                    # 각 학생들의 찍는 방식
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):           # 답을 비교해서 점수 계산
        if answers[i] == s1[i%5]:
            cnt1 += 1
        if answers[i] == s2[i%8]:
            cnt2 += 1
        if answers[i] == s3[i%10]:
            cnt3 += 1
    max_score = max(cnt1, cnt2, cnt3)       # 가장 높은 점수
    if max_score == cnt1:                   # 가장 높은 점수인 학생을 answer에 append
        answer.append(1)
    if max_score == cnt2:
        answer.append(2)
    if max_score == cnt3:
        answer.append(3)
    return answer
