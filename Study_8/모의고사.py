#테스트 케이스는 통과했지만 제출하기는 통과하지 못했습니다..

#i번 문제에서 수포자가 찍은 값
#1번 수포자 -> 12345... -> (i%5), 0일때는 5
#2번 수포자 -> 21232425... -> i%2==1이면 2, 짝수일때는 i%8이 2->1, 4->3, 6->4, 8->5
#3번 수포자 -> 3311224455... -> i%10이 (1,2->3 / 3,4->1 / 5,6->2 / 7,8->4 / 9,0->5)

def solution(answers):
    answer = []
    score = [0, 0, 0] #수포자들의 점수
    max_score = 0 #가장 높은 점수

    #1,2,3번의 수포자 각각의 점수를 계산한다
    for i, ans in enumerate(answers):
        num = [0, 0, 0]
        #1번 수포자가 찍은 값
        num[0] = (i+1) % 5
        if num[0] == 0: num[0] = 5

        #2번 수포자가 찍은 값
        if (i+1)%2 == 1: num[1] = 2
        else:
            num[1] = (i+1)%8
            if num[1]==2: num[1] = 1
            elif num[1] == 4: num[1] = 3
            elif num[1] == 6: num[1] = 4
            elif num[1] == 8: num[1] = 5

        #3번 수포자가 찍은 값
        num[2] = (i+1)%10
        if num[2]==1 or num[2]==2: num[2]=3
        elif num[2]==3 or num[2]==4: num[2]=1
        elif num[2]==5 or num[2]==6: num[2]=2
        elif num[2]==7 or num[2]==8: num[2]=4
        elif num[2]==9 or num[2]==0: num[2]=5

        #점수 확인
        for j in range(3):
            if ans ==num[j]: score[j] = score[j] +1

    max_score = max(score) #가장 높은 점수를 확인

    #가장 높은 점수와 점수가 같다면 리스트에 삽입 *1,2,3순으로 삽입하므로 정렬이 불필요
    for i in range(3):
        if max_score == score[i]: answer.append(i+1)

    return answer
