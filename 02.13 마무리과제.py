while True:
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 프로그램 종료")
    menu = int(input("원하는 기능의 번호를 입력하세요: "))

    if menu == 1 :
        firstNum = int(input('첫 번째 정수를 입력하세요: '))
        secondNum = int(input('두 번째 정수를 입력하세요: '))
        print(f'{firstNum}와 {secondNum}를 더하기 연산한 결과는 {firstNum + secondNum}입니다.')
    
    elif menu == 2:
        firstNum = int(input('첫 번째 정수를 입력하세요: '))
        secondNum = int(input('두 번째 정수를 입력하세요: '))
        print(f'{firstNum}와 {secondNum}를 빼기 연산한 결과는 {firstNum - secondNum}입니다.')
    
    elif menu == 3:
        firstNum = int(input('첫 번째 정수를 입력하세요: '))
        secondNum = int(input('두 번째 정수를 입력하세요: '))
        print(f'{firstNum}와 {secondNum}를 곱하기 연산한 결과는 {firstNum * secondNum}입니다.')
    
    elif menu == 4:
        firstNum = int(input('첫 번째 정수를 입력하세요: '))
        secondNum = int(input('두 번째 정수를 입력하세요: '))
        if secondNum == 0:
            print('연산이 불가합니다.')
        else:
            print('{0}와 {1}를 나누기 연산한 결과는 {div:.6f}입니다.'.format(firstNum, secondNum, div = float(firstNum / secondNum)))
    
    elif menu == 5:
        print('프로그램을 종료합니다.')
        break

    else:
        pass