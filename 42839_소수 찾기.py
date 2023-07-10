from itertools import permutations

def solution(numbers):
    answer = []                                   
    nums = [n for n in numbers]                   
    per = []  
    # 순열로 조합해서 리스트로 만들기
    for i in range(1, len(numbers)+1):           
        per += list(permutations(nums, i))
    # int로 변환
    new_nums = [int(("").join(p)) for p in per]   

    # 소수 확인
    for n in new_nums:                            
        if n < 2:                                
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):       
            if n % i == 0:                        
                check = False
                break
        if check:
            answer.append(n)                     

    return len(set(answer))                       
