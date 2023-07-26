from itertools import product

def solution(word):
    words = 'AEIOU'
    
    all_strings = []
    
    #모든 경우의 단어 생성, 
    for i in range(1, 6):
        for p in product(words, repeat=i):
            s = ''.join(p)
            all_strings.append(s)
    
    #생성된 단어 정렬
    all_strings.sort()
    
    #생성된 단어에서 입력된 단어의 인덱스 추출
    index = all_strings.index(word)
    
    return index + 1
