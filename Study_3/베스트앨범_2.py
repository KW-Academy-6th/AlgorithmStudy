from collections import defaultdict

def solution(genres, plays):
    answer = []

    total_play = defaultdict(int)           # 장르와 해당 장르의 총 재생 횟수를 저장하는 딕셔너리, default type: int
    genre_play = defaultdict(list)          # 노래의 장르와 고유 번호, 재생 횟수를 저장하는 딕셔너리, default type: list

    for i, (genre, cnt) in enumerate(zip(genres, plays)):
        total_play[genre] += cnt            # total_play에 각 장르(key)의 value에 재생 횟수들을 더한다
        genre_play[genre].append((i, cnt))  # genre_play에 각 장르(key)의 value에 고유 번호와 재생 횟수
를 저장

    # total_play에서 총 재생 횟수를 기준으로 내림차순으로 sort
    for genre, _ in sorted(total_play.items(), key=lambda x: x[1], reverse = True):
        # genre_play에서 장르에 대해 재생 횟수를 기준으로 내림차순으로 sort > 리스트 값 두 개로 설정
        for i, cnt in sorted(genre_play[genre], key=lambda x: x[1], reverse = True)[:2]:
            answer.append(i)

    return answer
