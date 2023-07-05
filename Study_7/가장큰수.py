def solution(numbers):
    numbers = list(map(str, numbers)) # numbers의 요소를 str로 변환
    numbers.sort(key=lambda x: x*3, reverse=True) # 원소는 0 이상 1,000 이하이므로 3번 반복
    answer = str(int(''.join(numbers))) # 0000 같은 경우를 0으로 변환하기 위해 int로 변환 후 다시 str로 변환
    return answer
