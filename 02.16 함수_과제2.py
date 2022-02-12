num = int(input('양의 정수 입력(음수입력시 종료) : '))

if num < 0:
    pass    #종료

binaryNum = ''
callNum = 0


def binary(num):
    #전역변수 선언
    global binaryNum
    global callNum
     
    callNum += 1

    if num // 2 > 0:
        binaryNum += str(num % 2)
        num = num // 2

        return binary(num)

    else:
        binaryNum += str(num % 2)
        return 

binary(num)
print(f'{num}의 이진수 : {binaryNum[::-1]}  binary() 함수 반복횟수 : {callNum}')