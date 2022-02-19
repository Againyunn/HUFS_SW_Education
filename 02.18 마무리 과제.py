

def investment(seed, date, calculate):
	firstSeed = seed #값이 변경되기 전 비교할 대상 설정

	for i in range(date):
		change = seed * (calculate[i]/100)
		seed += change

	result = int(seed - firstSeed)
	print(result)

	if result > 0:
		print('이득입니다.')

	if result == 0:
		print('본전입니다.')
	
	if result < 0:
		print('손해입니다.')


seed=int(input('투자 액수를 입력하세요:'))
date=int(input('투자한 날짜 수를 입력하세요:'))
calculate=[] #퍼센트 기록
for i in range(date):
	thisData=int(input(f'{i+1}일차 변동 데이터를 입력하세요:'))
	calculate.append(thisData)

investment(seed, date, calculate)