import datetime

carNum = int(input('차량번호 입력 : '))

#오늘 시각 추출
today = datetime.datetime.now()

#x = datetime.datetime.now() 메서드는 
# x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond 를 객체(x)에 저장
# 참고: https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html

#day만 분리
day= today.day

#오늘(day)의 홀/짝수 판별
evenOdd = "홀수"
if day % 2 == 0:
    evenOdd = "짝수"

#주차 가능 여부 확인
can = ' 불'
if evenOdd == "짝수" and carNum % 2 == 0:
    can = ''
if evenOdd == "홀수" and carNum % 2 != 0:
    can = ''

print(f'오늘은 {day}로 {evenOdd}날로 주차{can}가능합니다.')