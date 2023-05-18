from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0
    
    while queue:
        maxPriority = max(queue) #현재 큐에 존재하는 가장 우선순위가 빠른 수
        
        currentProcess = queue.popleft()
        location -= 1 
        
        #현재 큐가 가장 우선순위가 높지 않다면, 다시 큐의 뒤에 삽입
        if currentProcess != maxPriority:
            queue.append(currentProcess)
            #구하기를 원하는 큐가 가장 앞이었다면, 뒤로 이동하며 위치 변경
            if location < 0:
                location = len(queue) -1
        #현재 큐가 가장 우선 순위가 높다면, 실행 숫자를 1증가시킨다
        else:
            answer += 1
            #구하기를 원하는 큐가 가장 앞이었다면 결과 출력
            if location < 0:
                return answer
