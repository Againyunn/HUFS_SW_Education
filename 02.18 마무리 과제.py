
def invest(a,b,c):
	original=a
	for x in range(b):
		a=a+a*(c[x]/100)

	total=a-original
	print('%d'%(total))
	if total > a:
		print('이득입니다.')
	elif total == a:
		print('본전입니다.')
	else:
		print('손해입니다.')
	

a=int(input('투자 액수를 입력하세요:'))
b=int(input('투자한 날짜 수를 입력하세요:'))
c=[]
for i in range(b):
	data=float(input('%d일차 변동 데이터를 입력하세요:'%(i+1)))
	c.append(data)

invest(a,b,c)