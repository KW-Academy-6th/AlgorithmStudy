#https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(2, n): #2부터 n-1까지
        if n % i == 1: #나누었을때 나머지가 1이면
            return i #나눈 값 반환
