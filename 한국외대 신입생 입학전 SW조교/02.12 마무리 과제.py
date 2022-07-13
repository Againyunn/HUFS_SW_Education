start_day = 2
last_day = 31

print('\tS\tM\tT\tW\tT\tF\tS')
for i in range(start_day):          #시작하는 위치 지정
    print('\t', end='')

for i in range(1, last_day+1):      #총 한 달의 일자를 for문을 돌며 반환
    if (start_day + i) % 7 != 0:    #6일차까지는 한 주에 출력
        print('\t%d' %i, end='') 
    elif (start_day + i) % 7 == 0:  #7일차를 식별하여 출력 후 한 줄 띄우기
        print('\t%d\n' %i)