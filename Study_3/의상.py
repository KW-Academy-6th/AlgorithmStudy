#https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    
    #옷의 종류를 key로 각 종류별 옷의 개수를 value로 가지는 딕셔너리 생성.
    clothes_dict = {}
    for name, kind in clothes:
        if clothes_dict.get(kind):
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    #(종류의 개수+1)을 서로 곱한 뒤 1을 빼 값을 구합니다.
    answer = 1
    for value in clothes_dict.values():
        answer *= (value +1)
        
    return answer -1
