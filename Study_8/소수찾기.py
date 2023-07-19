from itertools import permutations

# 입력 받은 수가 소수이면 1을, 소수가 아니면 0을 반환하는 함수
def is_prime_num(num):
    if num == 1 or num == 0:
        return 0
    # 2부터 num의 절반까지의 숫자로 나누어지는지 확인하여 소수 여부를 판단
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    len_num = len(numbers)
    nums_set = set()
    
    # 모든 경우의 수 생성 후 소수인지 검사
    # 입력 숫자가 한 자리 수인 경우
    if len_num == 1:
        return is_prime_num(int(numbers))
    # 입력 숫자가 여러 자리 수인 경우
    else:
        # 1부터 len_num까지의 길이의 모든 순열 생성
        for i in range(1, len_num + 1):
            # i 길이의 순열 생성
            perms = list(permutations(numbers, i))
            for perm in perms:
                # 순열을 정수로 변환하여 중복을 없애기 위해 집합인 nums_set에 추가
                int_num = int(''.join(perm))
                nums_set.add(int_num)
        
        # nums_set의 숫자들이 소수인지 검사
        for num_set in nums_set:
            answer = answer + is_prime_num(num_set)

    return answer
