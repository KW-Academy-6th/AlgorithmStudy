#https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [] #연속된 수를 제거한 원소가 저장될 스
    for i, value in enumerate(arr):
        if i == 0 or answer[-1] != value: #첫번째 값이거나, 이전값과 다르다
            answer.append(value) #연속된 수가 아니므로 스텍에 저장
    return answer
