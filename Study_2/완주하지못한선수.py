def solution(participant, completion):
    answer = ''
    player = dict.fromkeys(participant, 0)
    # participant를 key로 가지고 모든 value가 0인 딕셔너리 생성
    for i in participant:
        player[i] += 1
        # participant에 존재하는 key의 value에 전부 +1
    for i in completion:
        player[i] -= 1
        # completion에 존재하는 key의 value에 전부 -1
    for key, value in player.items():
        if value != 0:
            answer = key
            # 딕셔너리의 튜플들 중 value가 0이 아닌 경우의 key
            # 완주한 선수라면 0+1(첫번째for)-1(두번째for)=0
    return answer
