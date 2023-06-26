import heapq

def solution(operations):
    answer = []                                     # 최댓값, 최솟값을 저장할 리스트
    calculate = []                                  # 계산을 위한 리스트
    op = []                                         # 명령을 저장할 리스트
    for i in operations:                
        op.append(i.split())                        # operation을 알파벳과 숫자로 나누어 저장
    for j in op:
        if j[0] == "I":                             # 명령어가 I인 경우
            heapq.heappush(calculate, int(j[1]))    # 숫자를 calculate 리스트에 heappush
        elif j[0] == "D":                           # 명령어가 D인 경우
            if len(calculate) == 0:                 # 리스트가 비어있으면 continue
                continue
            elif j[1] == "1":                       # 숫자가 1인 경우 최댓값 삭제
                calculate.remove(max(calculate))
            elif j[1] == "-1":                      # 숫자가 -1인 경우 최솟값 삭제 (heappop)
                heapq.heappop(calculate)
    if len(calculate) == 0:                         # calculate 리스트가 비어있으면 [0, 0]    
        answer = [0, 0]             
    else:                                           # calculate 리스트가 비어있지 않으면 [최댓값, 최솟값]
        answer = [max(calculate), min(calculate)]
    return answer
