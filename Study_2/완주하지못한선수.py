#https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dict_participant = {}
    
    for x in participant:
        if x in dict_participant:
            dict_participant[x] += 1
        else:
            dict_participant[x] = 1  
    # {참여한 선수의 이름 : 해당 이름을 가진 인원 수} 형태의 딕셔너리를 생성합니다.
    
    for x in completion:
        dict_participant[x] -= 1
        if dict_participant[x] == 0:
            del dict_participant[x]
    # 이전에 만든 딕셔너리에서 완주자의 이름과 같은 key값을 가지는 value 값을 1씩 빼준다
    # value가 0인 것은 해당 이름을 가진 인원수가 0이 된것이므로 딕셔너리에서 삭제합니다.
    
    for key in dict_participant.keys():
        return key
    # 딕셔너리에 남아있는 미 완주 자의 이름(키 값)을 출력 합니다.
