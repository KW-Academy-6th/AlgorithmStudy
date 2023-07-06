def solution(citations):
    citations.sort(reverse = True) #논문 인용 횟수를 내림차순 정렬
    
    for i, citation in enumerate(citations):
        if i + 1  == citation: # i+1과 인용수가 같은경우 인용수 리턴 [6, 5, 3, 1, 0] 같은 경우
            return citation
        elif i + 1 > citation: # i+1이 인용수 보다 클 경우 i리턴 [0, 0, 0], [8, 7, 6, 5, 0] 같은 경우
            return i
        
    return len(citations) #모든 논문의 인용수가 논문의 수보다 클때  [5, 5, 5] 
