def solution(array, commands):
    answer = []
    for cmd in commands:
        cal = sorted(array[cmd[0]-1:cmd[1]])        # array를 cmd에서 지정한만큼 slice
        answer.append(cal[cmd[2]-1])                # cmd에서 지정한 index 값을 answer에 저장
    return answer
