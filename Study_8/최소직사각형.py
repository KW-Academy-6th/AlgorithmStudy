def solution(sizes):
    max_w = 0 #지갑의 가로길이
    max_h = 0 #지갑의 세로길이
    
    for card in sizes:
        card.sort() #명함의 작은 쪽 길이가 앞으로 오도록 정렬
        if card[0] > max_w: max_w = card[0] #이전의 작은 쪽 길이보다 크다면 바꿔 저장
        if card[1] > max_h: max_h = card[1] #이전의 큰 쪽 길이보다 크다면 바꿔 저장

    return max_w * max_h
