#https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 장르의 재생 횟수 합계
    # defaultdict(int)를 사용해 키가 존재하지 않는 경우 0을 값으로 가지는 항목을 자동 생성
    count_dict = defaultdict(int)
    for genre, play in zip(genres, plays):
        count_dict[genre] += play
    # 재생 수가 많은 장르순으로 정렬
    sorted_count_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))

    # 장르를 키로 (곡 고유 번호, 재생 횟수)를 값으로 가진 딕셔너리 생성 
    song_dict = defaultdict(list)
    for i, genre in enumerate(genres):
        song_dict[genre].append((i, plays[i]))
        
    # 장르별 곡 리스트를 재생수 내림차순으로 재생수가 같은 경우 고유번호 오름차순으로 정렬
    for song_list in song_dict.values():
        song_list.sort(key=lambda x: x[0])
        song_list.sort(key=lambda x: x[1], reverse=True)

    # 재생 수가 많은 장르 순으로 장르별 최대 2곡 선택
    for genre in sorted_count_dict.keys():
        answer.extend([songID for songID, play in song_dict[genre][:2]])

    return answer
