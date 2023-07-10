def solution(sizes):
    max_arr = []
    min_arr = []
    answer = 0
    for i in range(0, len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            max_arr.append(sizes[i][0])
            min_arr.append(sizes[i][1])
        else:
            max_arr.append(sizes[i][1])
            min_arr.append(sizes[i][0])
    answer = max(max_arr) * max(min_arr)
    return answer
