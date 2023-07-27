from itertools import product

def solution(word):
    answer = 0
    pr = []
    alpha = ['A', 'E', 'I', 'O', 'U']                   # 단어를 만들 알파벳
    for i in range(1, 6):                               # 조합 만들기
        pr += list(product(alpha, repeat=i))
    word_list = [''.join(map(str, p)) for p in pr]      
    word_list.sort()                                    # sort
    answer = word_list.index(word) + 1                  # 0부터 시작하므로 +1
    return answer
