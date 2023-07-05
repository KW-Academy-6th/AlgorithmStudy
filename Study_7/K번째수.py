def solution(array, commands):
    answer = [] #정답을 저장할 리스트
    
    #command를 차례로 실행한다
    for command in commands:
        evaluation_list = array[command[0]-1:command[1]] #command에 따라 히스트을 슬라이스 한다
        evaluation_list.sort() #슬라이스된 리스트을 정렬한다
        answer.append(evaluation_list[command[2]-1]) #정렬된 리스트에서 원하는 위치의 값을 뽑아 제출할 리스트에 삽입한다

    return answer
