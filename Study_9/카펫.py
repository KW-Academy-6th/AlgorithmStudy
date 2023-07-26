def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for width in range(1, area+1):
        if (area / width) % 1 == 0:     # area를 어떤 값으로 나눴을 때 나머지가 0인 경우
            height = area / width       # height 설정
            if width >= height:         # width가 height보다 커야 한다
                if 2 * width + 2 * height == brown + 4:   # 조건 만족 시 answer에 추가
                    answer.append(width)
                    answer.append(height)
                    break
    return answer
