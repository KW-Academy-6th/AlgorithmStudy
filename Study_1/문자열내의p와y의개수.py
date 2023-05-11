#https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    # 받은 문자열을 모두 소문자로 변환 후 개수를 세서 비교한다.
    return True if s.lower().count('p') == s.lower().count('y') else False
