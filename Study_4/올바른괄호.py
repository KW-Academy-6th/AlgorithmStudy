def solution(s):
    answer = True
    test = []
    for i in s:
        if i == '(':                            # 여는 괄호일 경우
            test.append(i)                      # test에 append
        elif i == ')' and len(test) == 0:       # 닫는 괄호인데 test가 빈 경우
            answer = False
            break                               # answer에 False 넣고 반복 멈춤
        elif i ==')' and len(test) > 0:         # 닫는 괄호인데 test에 값이 있을 경우
            if test.pop() == '(':               # test에 가장 마지막 값이 여는 괄호인 경우
                continue                        # 계속 반복 실행
        else:
             print("error")
    if len(test) > 0:
        answer = False                          # 리스트에 값이 남아있는 경우 False
    return answer
