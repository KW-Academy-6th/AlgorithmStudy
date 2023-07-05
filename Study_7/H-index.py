def solution(citations):
    answer = 0
    citations.sort()            # 오름차순으로 sort
    len_c = len(citations)      # 전체 논문 개수
    for i in range(len_c):
        # h번 이상 인용된 논문이 h편 이상이어야 하므로 마지막부터 h번째 논문이 h번 이상 인용되었는지 확인
        # (ex. [0,1,3,5,6]인 경우 정렬된 상태이므로 0이 5 이상이면 나머지도 다 5 이상이 된다)
        if citations[i] >= len_c-i:
            return len_c-i
    return 0                    # 모든 논문의 인용 수가 0인 경우
