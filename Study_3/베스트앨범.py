def solution(genres, plays):
    answer = []
    num = dict.fromkeys(genres, 0)          # 장르와 장르의 총 재생 횟수를 저장할 딕셔너리
    size = dict()                           # 각 노래의 고유 번호와 재생 횟수를 저장할 딕셔너리

    for i, j in zip(genres, plays):
        num[i] += j                         # num 딕셔너리의 각 장르(key)에 재생 횟수들을 더한다
    num_sort = sorted(num.items(), key=lambda x: x[1], reverse=True)
    num_key = [x[0] for x in num_sort]      # 총 재생 횟수로 내림차순 sort하고 튜플 > 리스트로 변환

    for m in num_key:                       # 장르 개수만큼 반복
        for n in range(len(genres)):        # 노래 개수만큼 반복
            if genres[n] == m:              # 노래의 장르가 현재 출력 중인 장르인 경우
                size[n] = plays[n]          # 노래 고유 번호를 key, 재생횟수를 value로 딕셔너리에 저장
        size_sort = sorted(size.items(), key=lambda x: x[1], reverse=True)
        size_key = [x[0] for x in size_sort]    # 재생 횟수로 내림차순 sort하고 튜플 > 리스트로 변환
        for k in size_key[:2]:                  # 전체 리스트에서 두 개까지만 반복
            answer.append(k)
        size.clear()                            # 딕셔너리 clear

    return answer
