def solution(nums):
    nums_len = len(nums) // 2  # 가져갈 수 있는 폰켓몬(N/2)
    phonekemon = {}  # 폰켓몬의 종류, 수를 저장할 딕셔너리
    for i in nums:
        if i in phonekemon:  # 배열 값이 딕셔너리 안에 존재하는 경우
            phonekemon[i] += 1  # value에 +1
        else:  # 배열 값이 딕셔너리 안에 존재하지 않는 경우
            phonekemon[i] = 1  # 딕셔너리에 tuple 생성
    if nums_len <= len(phonekemon.keys()):
        return nums_len
    # 딕셔너리의 키 개수가 N/2보다 크거나 같다면 N/2 값 리턴
    # 가져갈 폰켓몬의 개수가 가져갈 수 있는 폰켓몬 개수를 넘으면 안됨
    else:
        return len(phonekemon.keys())
    # 딕셔너리의 키 개수가 N/2보다 작다면 키 개수 리턴
