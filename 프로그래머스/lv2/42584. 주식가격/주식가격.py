def solution(prices):
    k=len(prices)
    answer=[0]*k
    for i in range(k):
        for j in range (i+1,k):
            answer[i]+=1
            if prices[j] < prices[i]:# 타겟으로 한 애보다 작은애일때가 가격이 떨어졌을때
                break
    return answer