from itertools import permutations

def solution(k, dungeons):
    answer = 0

    #던전을 가는 순서의 모든 경우의 수 생성
    for order in permutations(dungeons):
        fatigue = k
        num_dungeons = 0

        #해당 순서로 던전을 방문할시 탐험 가능한 던전 수
        for dungeon in order:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                num_dungeons += 1
            else:
                break

        #가장 많이 탐험 할 수 있는 수 구하기
        answer = max(answer, num_dungeons)

    return answer
