def solution(citations):
    answer = 0
    citations.sort(reverse=True)
#65310
    n=len(citations)
        
    for i in range(n):  
        # H-Index가 주어진 배열에 포함된 값이 아닐 수 있다는 부분을 생각하지 못하신 것 같습니다.
        if  citations[0]==0:
            break
        if n<=citations[i]: 
            answer=n   
            
        if citations[i]<=i:
            answer=i
            break
            
    return answer
# 100 100 100