rawNum = int(input('출력 줄수 입력 : '))

total = 1 + 2 *rawNum   #총 출력될 열의 칸 개수
thisStar = total//2 #해당 열의 첫번째 *이 출력될 위치(초기값)

star = '*'

# # 단일 for문 사용
# for i in range(rawNum):
#     blank = ' ' * (thisStar - i)
#     print(f'{blank}{star}{blank}')
#     star += '**'

# 이중 for문 사용
for i in range(rawNum):
    blank = ''              #빈칸 변수 초기화
    
    for j in range(total):      #각 열의 라인 출력
        if j <= (thisStar - i):
            blank += ' '
        
    print(f'{blank}{star}{blank}')
    star += "**"
