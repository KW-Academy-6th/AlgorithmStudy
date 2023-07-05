def solution(numbers):
    answer = ''
    # 입력으로 받은 숫자 리스트를 string으로 타입 변환 > 앞 자리 수부터 비교하기 위해
    numbers = list(map(str, numbers))
    # (ex. 2가 20보다 앞으로 와야하므로) 한 자리 수도 세 자리수가 되도록 문자열을 세 번 반복하여 sort
    numbers.sort(key=lambda x: x*3, reverse=True)
    for num in numbers:
        answer += num               # string 이어붙이기
    return str(int(answer))         # 0만 있는 경우 대비
