num=int(input("출력 줄수 입력:"))

for i in range(1, num+1): #i는 1부터 num까지의 정수
	print('{:(num-1)}') #첫 번째 * 앞의 공백 칸수는 "출력 줄수"보다 1 작은 수이므로 num-1만큼의 공백 입력
for j in range(1, num+1): #j는 1부터 num까지의 정수
	print('*'*(num*2-1)) #각 줄의 * 개수는 (해당 줄 번호*2-1)이므로 그 개수만큼의 * 입력

# num = int(input())

# if num<=0:
# 	print('자연수가 아닙니다.')
# elif num%2==1:
# 	print('입력한 수 %d는 홀수입니다.'%num)
# elif num%2==0:
# 	print('입력한 수 %d는 짝수입니다.'%num)

# n = int(input("출력 줄수 입력 : "))
# for i in range(1,n+1):
# 	for j in range(1,n+1-i):
# 		print(" ", end="")
# 	for j in range(2*i-1):
# 		print("*", end="")
# 	print()
# num=int(input('출력 줄수 입력 : '))
# for i in range(1,num+1):
# 	for j in range(1,num+1-i):
# 		print(' ',end='')
# 	for j in range(1,i+1):
# 		print('*',end='')
# 	print()


# sum=0
# i=9
# while sum <=100:
#     sum+=i
#     if sum + i <100:
#         print(i,'+',end='')
#         i += 9
#     else:
#         print(i,'=',end='')
#         break
    
# print(sum)


# sum=0
# i=9
# while True:
# 	sum+=i
# 	if sum + i < 100:
# 		print(i, '+', end=' ')
# 		i+=9
# 	else:
# 		print(i, '=', end=' ')
# 		break

# print(sum)