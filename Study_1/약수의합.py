#https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    
    for i in range(n, 0, -1):
        if n % i == 0:
            answer += i
            
    return answer
