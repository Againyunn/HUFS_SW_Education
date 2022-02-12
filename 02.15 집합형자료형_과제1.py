phoneNum = []
for i in range(3):
    tmpDic ={}
    name = input('이름: : ')
    tel = input("전화 : ")
    tmpDic['name'] = name
    tmpDic['tel'] = tel
    phoneNum.append(tmpDic)

while True:
    rule = input('1. 검색   2. 종료 :')
    if rule == '1':
        searchName = input('검색할 이름 : ')
         
        #검색할 이름이 phoneNum 안에 있는 지 식별하기 위한 코드
        if next((item for item in phoneNum if item['name'] == searchName), False): 
            result = next((item for item in phoneNum if item['name'] == searchName), False)
            print(f'{result["name"]} : {result["tel"]}')
        
        else:
            print(f'{searchName}의 전화번호는 저장되어 있지 않습니다!')
    
    elif rule == '2':
        print('리스트 내용')
        for i in range(len(phoneNum)):
            print(phoneNum[i])
        break
    
    else:
        print('잘못된 번호를 입력함!!!')
