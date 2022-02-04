score = input("정수 입력 : ")

#문자열이 숫자인지 판별하는 메서드
# isdecimal() :int형으로 변환가능한지 판별
# isdight()   :숫자의 형태인지 판별
# isnumeric() :숫자값 표현에 해당하는 문자열인지 판별

if score.isdecimal() == True:
    score= int(score)
    if score > 100:
        print("숫자 범위 오류!!!")
    elif score >= 80:
        print("통과!!!")
    elif score >= 60:
        print("재시험!!!")
    else:
        print("과락!!!")

else:
    print("숫자를 입력해야 합니다")