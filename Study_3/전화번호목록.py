def solution(phone_book):
    phone = set()           # 전화번호를 저장할 set
    check = []              # 접두사 확인을 위한 리스트
    for i in phone_book:    # phone_book의 값들을 set과 리스트에 저장
        phone.add(i)
        check.append(i)

    answer = True                       # 접두어 유무를 판단할 변수
    for ph in check:                    # check 리스트에서 번호 가져오기
        for j in range(1, len(ph)):     # 해당 번호의 길이만큼 반복
            num = ph[:-j]               # 번호를 분할 > 0~(번호길이-j)
            if num in phone:            # 분할한 숫자가 다른 번호와 동일한 경우
                answer = False          # 접두어이므로 False
                break
    return answer
