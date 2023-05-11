#https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math #math.ceil을 사용하기 위해

def solution(progresses, speeds):
    answer = [] #답을 저장한 리스트
    queue = [] #작업이 끝나기 까지 남은 일 수를 저장할 
    count = 0 #동시에 배포가 되는 기능의 개수를 세기 위한 변수
    
    #나누기와 올림을 이용해 작업이 끝나기까지 걸리는 일 수를 큐에 저장
    for progress, speed in zip(progresses, speeds):
        queue.append(math.ceil((100-progress)/speed))
    
    #최근의 가장 오래 걸리는 작업의 일 수를 저장할 버퍼, 첫번째 값으로 초기화 한다
    tem = queue[0]
    
    #큐의 길이만큼 반복
    for i in range(len(queue)):
        if queue[i] > tem: #현재 값의 버퍼의 값보다 큰경우
            tem = queue[i] #현재 큐의 값으로 버퍼 갱
            answer.append(count) #동시에 배포되는 기능의 개수 입
            count = 1 #초기와 (현재 큐는 비교에만 사용되고 이전의 작업에 포함되지 않았기 때문에 1로)
        else: #현재 큐의 값이 버퍼보다 작은경우
            count += 1 #동시에 배포되는 기능의 수  + 1
            
        if i + 1 == len(queue): #마지막 반복이라면
            answer.append(count)

    return answer
