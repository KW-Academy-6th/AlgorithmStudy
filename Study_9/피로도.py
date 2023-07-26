from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons, len(dungeons)):     # 모든 순서 조합
        count = 0
        time = k
        for need, use in i:
            if need <= time:        # 필요 피로도가 현재 피로도보다 작거나 같은 경우
                time -= use         # 소모 피로도 빼기
                count += 1          # 던전을 한번 돌았으므로 count +1
        if count >= answer:         # count가 현재 answer보다 큰 경우
            answer = count          # update
    return answer
