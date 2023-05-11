#https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    #각 번호를 키로, 번호의 길이를 value로 하는 딕셔너리 생성
    hash_phone_book = {item: len(item) for item in phone_book}
    
    #전화번호를 순서대로 불러온다
    for phone_number in hash_phone_book:
        #불러온 전화번호의 첫번째 번호 부터 차례로 늘려가며 해당 번호가 딕셔너리에 존재하는지 검색
        for i in range(1, hash_phone_book[phone_number]):
            if hash_phone_book.get(phone_number[:i]):
                return False
            
    return True
