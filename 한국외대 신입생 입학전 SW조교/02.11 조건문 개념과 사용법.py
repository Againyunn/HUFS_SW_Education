num = int(input())

if num <= 0 :
    print("자연수가 아닙니다.")
else:
    if num % 2 != 0:
        print("홀수입니다.")
    else:
        print("짝수입니다.")