import math

def solution(brown, yellow):
    width = 0 #카펫의 가로
    height = 0 #카펫의 세로
    carpet_edge = 0 #카펫 둘레의 길이
    total_carpet = brown + yellow #전체 격자의 개수
    
    min_width = math.ceil(math.sqrt(total_carpet)) #최소 가로의 길이
    
    #최소 가로의 길이 부터 1씩 증가하며 세로의 길이를 구하고, 조건에 맞을시 정답 리턴
    width = min_width
    while 1:
        height = total_carpet / width
        #테두리의 길이인 ((가로길이 + 세로길이) * 2) - 4가 갈색 격자의 수가 같으면 정답
        if brown == ((width + height) * 2) - 4:
            return [width, height]
        width = width + 1
