def solution(answers):
    first_std = 0
    second_std = 0
    third_std = 0
    f_std_list = [1, 2, 3, 4, 5] * 8
    s_std_list = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    t_std_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4
    answer = []
    idx = 0
    for i in range(0, len(answers)):
        if (i % 40 == 0) and (i != 0) :
            idx += 1
        if f_std_list[i-(idx*40)] == answers[i]:
            first_std += 1
        if s_std_list[i-(idx*40)] == answers[i]:
            second_std += 1        
        if t_std_list[i-(idx*40)] == answers[i]:
            third_std += 1        
    
    if first_std > second_std :
        if first_std > third_std:
            answer.append(1)
        elif first_std <third_std:
            answer.append(3)
        else:
            answer.append(1)
            answer.append(3)
    elif first_std < second_std:
        if second_std > third_std:
            answer.append(2)
        elif second_std <third_std:
            answer.append(3)
        else:
            answer.append(2)
            answer.append(3)
    else :
        if first_std > third_std:
            answer.append(1)
            answer.append(2)
        elif first_std < third_std:
            answer.append(3)
        else:
            answer.append(1)
            answer.append(2)
            answer.append(3)
    return answer
