#https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    
    str_n = str(n) #문자열로 변환
    list_n = list(str_n) #문자열을 리스트로 변환해서 한 자리씩 끊는다

    return sum(map(int, str_n)) #map을 이용해 하나씩 int로 변환해 더한다
