from collections import deque

def solution(prices):
    answer = []
    pricesQueue = deque(prices) #가격정보를 가지도있는 큐
    lenPrices = len(prices) #주식의 개수
    
    #주식을 순차적으로 반복
    for i in range(lenPrices):
        count = 0
        currentQueue = pricesQueue.popleft() #현재 확인할 주식의 가격
        #현재 확인할 주식의 가격과 이후의 가격과의 순차적 비교
        for j in range(i+1, lenPrices):
            count += 1
            if currentQueue > prices[j]:
                break
        answer.append(count)
    return answer
