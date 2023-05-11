#https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    
    for value in s:
        if not stack and value == ')': #첫 입력이 )일때 False 반
            return False
        elif value == ')': #입력이 )일때 이전 입력 삭제
            stack.pop()
        else: #입력이 (일때 스텍에 입
            stack.append(value)
    
    if not stack: #작업이 끝났을때, 스텍이 비어있다면 올바른 괄호
        return True
    return False
