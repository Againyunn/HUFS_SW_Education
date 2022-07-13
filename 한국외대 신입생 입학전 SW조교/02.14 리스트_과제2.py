myList = []

while True:
    ##default print
    print('********************')
    print('1. 이름 추가')
    print('2. 이름 삭제')
    print('3. 이름 수정')
    print('4. 종료')
    menu = int(input('메뉴 선택 : '))

    ##이름 추가
    if menu == 1:
        inputName = input('이름 : ')

        if myList.count(inputName) == 0:
            myList.append(inputName)
            print(myList)
        else:
            print('이미 있는 이름')
    
    ##이름 삭제
    elif menu == 2:
        deleteName =  input('이름 : ')

        if myList.count(deleteName) > 0:
            myList.remove(deleteName)
            print(myList)
        else:
            print('해당 이름은 없음')

    ##이름 수정
    elif menu == 3:
        targetName = input('이름 : ')

        if myList.count(targetName) > 0:
            modifyingName = input('새이름 : ')
            myList[myList.index(targetName)] = modifyingName
            print(myList)
        else:
            print('해당 이름은 없음')
    
    elif menu == 4:
        break
    
    else:
        pass
