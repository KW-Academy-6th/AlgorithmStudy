def solution(name, yearning, photo):
    answer = []
    for peoples in photo:
        result = 0
        for people in peoples:
            if people in name:
                result += yearning[name.index(people)]
        answer.append(result)

    return answer