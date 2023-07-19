from itertools import permutations

def solution(numbers):
    answer = 0
    slice_number = [n for n in numbers]         # 숫자를 한자리씩 slice
    permutate = []
    # slice된 숫자들을 조합, 중복된 값 제거
    for i in range(1, len(slice_number)+1):
        permutate += list(permutations(slice_number, i))
    number_list = set([int(''.join(map(str, p))) for p in permutate])
    for num in number_list:
        prime = True            # 소수인지 판별
        if num < 2:             # 숫자가 2 미만이면 소수가 아님
            continue
        for j in range(2, num):
            if num % j == 0:    # 나눠지는 값이 있다면 판별 변수를 바꾸고 break(소수X)
                prime = False
                break
        if prime:               # 소수인 경우 answer에 +1
            answer += 1
    return answer
