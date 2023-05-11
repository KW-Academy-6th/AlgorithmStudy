#https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    sumNumber = 0
    for i in range(0, n):
        sumNumber += x #0부터 x씩 증가합니다.
        answer.append(sumNumber) #증가한 숫자를 리스트에 하나씩 입력 합니다.
    return answer
