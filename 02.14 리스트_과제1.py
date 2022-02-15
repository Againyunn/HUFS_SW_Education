thisList = []

while True:
    num = int(input("정수 입력 : "))
    
    if num == 0:        #0입력 시 현재 리스트의 값들 출력
        print(thisList)

        ## 현재 리스트의 값을 역순으로 출력
        print('\n역순 :', end='')
        for i in range(len(thisList), 0, -1):
            print(f'{thisList[i-1]} ', end='')

        ##삽입할 정수 값 받아 삽입 후, 출력
        inputNum = int(input('\n\n삽입 정수 : '))
        indexNum = int(input('삽입할 인덱스 : '))
        if indexNum <= len(thisList):           #기존 리스트의 길이 내에 입력받은 인덱스가 있는 경우
            thisList.insert(indexNum,inputNum)
        else:                                   #기존 리스트의 길이보다 입력받은 인덱스가 더 큰 경우(삽입 불가)
            print('index의 범위에 맞지 않습니다!!!')
        print(thisList)     

        ##삭제할 정수 값 받아 삭제 후, 출력
        deleteNum = int(input('\n삭제할 정수 : '))
        if thisList.count(deleteNum) > 0:
            thisList.remove(deleteNum)
        else:
            print(f'{deleteNum}는 존재하지 않습니다!')
        print(thisList)

        ##역순 리스트 생성 후 출력
        reversedList = []
        for i in range(len(thisList), 0, -1):
            reversedList.append(thisList[i-1])
        print(f'역순 : {thisList}')

        ##정렬 후 출력
        thisList.sort()     
        print(f'정렬 : {thisList}')

        break   #while문 무한 루프 종료

    else:               #0이 아닌 수 입력 시 리스트에 추가
        thisList.append(num)

    