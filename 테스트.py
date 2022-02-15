# 지금 발생한 문제는 break를 else에 걸어서, 한번이라도 검색이 되지 않으면 반복을 종료하기 때문에 첫번째 입력받은 name이 아닌, 다른 name을 입력받으면 정상적으로 출력이 안되는 상태에요:)
# 현 코드의 else문의 break를 삭제하면 2가지 문제가 잠재적으로 발생할거에요.
# 문제1. listA에 저장된 name을 검색했는데도 '{name}의 전화번호는 저장되어 있지 않습니다!' 오류가 계속 출력되는 상황
# 문제2. '{name}의 전화번호는 저장되어 있지 않습니다!' 오류는 한번만 출력되면 되는데, 2번이상 출력되는 상황
# 여기서 문제1의 원인은 if listA[i]['name'] == name:의 조건이 True인 값을 찾아도 반복문이 끝나지 않고 다음 인덱스까지 탐색하기 때문에 발생해요. 그래서 break를 통해 조건을 찾았다면 반복문을 탈출하게 만들면 될 거에요.
# 문제2의 원인은 else: 이 조건은 name이 listA에 없는 모든 경우에 오류 문장을 출력하라는 의미가 되어요.
# 그래서 if의 조건을 "반복을 다 끝냈을 때(i가 listA의 마지막 원소 값일 때)" 로 바꿔주고, '{name}의 전화번호는 저장되어 있지 않습니다!' 오류를 출력하면 될 거에요.




# 인덱스는 []로, 튜플은 ()로 둘러싸인 자료형이잖아요?
# 그래서 교수님께서 과제에 적어주신 것 같은 내용을 담은 튜플을 만들고, 물음에 따른 답을 출력하라는 의미에요.

# * 과제에서 요구하는 튜플 선언
# 튜플이름 = (["3+2", 5, 3], ["6/2", 3, 5], ["10-2", 8, 3], ["2의 3승", 8, 4], ["5-2*2", 1, 5])   #튜플이름 이라는 변수에 ["3+2", 5, 3], ["6/2", 3, 5], ["10-2", 8, 3], ["2의 3승", 8, 4], ["5-2*2", 1, 5] 의 원소가 튜플 자료형으로 담겨요!

# 여기서 예를 들어 ["3+2", 5, 3]를 뜯어보면,
# "3+2" : 문제(질문)
# 5       : 정답
# 3       : 배점
# 이런 식으로 다른 [ ] 안의 값들도 이해하고 각 질문 별로 입력받은 답을 "튜플이름"에 저장된 값과 비교해서 맞으면 배점만큼 점수를 누적하는 방식으로 과제를 풀면될거에요!


# 불필요한 for문 연산으로 인해 지금 문제가 생겼을 것 같아요

# * 수정해야 할 코드
# for j in range(len(t)):  #반복문을 삭제
#     if ans==t[j][1]:  # 각 값을 i로 변경
#         sum+=t[j][2]
#         correct+=1
#     elif ans!=t[j][1]:
#         ans+=0
#         correct+=0
# 지금은 바깥의 for문의 증감값(변화하는 값)인 i가 각 문제들을 가리키고 있는데, 두번째  for문을 한번 더 돌아서 j라는 인덱스로 모든 리스트의 값과 한번 더 비교하니까 
# 정상적인 정답을 비교하지 못해서, 점수를 제대로 기록하지 못하고 있어요.
# 그래서 for j in range(len(t)): 반복문을 삭제하고 아래 코드들의 j를 i로 바꾸면 문제가 해결될 거에요.



# listA=[]

# #입력받아 딕셔너리로 만든후 리스트 추가
# for i in range(3):
# 	a=input('이름 :')   
# 	b=input('전화 :')
# 	dic={'name':a, 'tel':b}
# 	# listA.append(dic)
# listA.extend(dic)
# print(listA)
# #listA 에다가 dic 를 삽입 또는 추가
	
  
# 	#[  {'name':'홍길동', 'tel':'123-432-4332'},
# 	#   {'name':'김철수', 'tel':'123-6789-3333'} 
# 	#  {.....}
# 	#]
	
# while True:
# 	menu = int(input('1:검색  2:종료 : '))
# 	if menu==1:
# 		name=input('검색할 이름 : ')
# 		for i in range(len(listA)):
# 			if listA[i]['name'] == name:
# 				print(listA[i]['tel'])
# 				break #break 추가
# 			elif i == len(listA) - 1:#listA[i][2]: #if조건문으로 바꾸고 조건을 새롭게 설정(i == 마지막 인덱스 번호 )
# 				print('%s의 전화번호는 저장되어 있지 않습니다!'%(name))
				
# 작성하신 코드를 확인했는데, 아마 2가지 문제로 인해서 질문하신 상황이 발생한 것 같아요.
# 문제1. listA에 저장된 name을 검색했는데도 '{name}의 전화번호는 저장되어 있지 않습니다!' 오류가 계속 출력되는 상황
# 문제2. '{name}의 전화번호는 저장되어 있지 않습니다!' 오류는 한번만 출력되면 되는데, 2번이상 출력되는 상황
# 여기서 문제1의 원인은 if listA[i]['name'] ==name:의 조건이 True인 값을 찾아도 반복문이 끝나지 않고 다음 인덱스까지 탐색하기 때문에 발생해요. 그래서 break를 통해 조건을 찾았다면 반복문을 탈출하게 만들면 될 거에요.
# 문제2의 원인은 else: 이 조건은 name이 listA에 없는 모든 경우에 오류 문장을 출력하라는 의미가 되어요.
# 그래서 if의 조건을 "반복을 다 끝냈을 때(i가 listA의 마지막 원소 값일 때)" 로 바꿔주고, '{name}의 전화번호는 저장되어 있지 않습니다!' 오류를 출력하면 될 거에요.

	# 	#for val in listA:
	# 	    #if val['name'] ==name
	# 		      #print(val['tel'])
	# elif menu ==2:
	# 	break
	# else:
	# 	print('잘못된 번호를 입력함!!!')



# listA = []

# for i in range(3):
#     a = input('이름 : ')
#     b = input('전화 : ')
#     dic = {'name':a, 'tel':b}
#     listA.append(dic)

# print(listA)
# while True:
#     menu = int(input('1: 검색 2: 종료 '))
#     if menu == 1:
#         name=input('검색할 이름 : ')
#         for i in range(len(listA)):
#             if listA[i]['name'] == name:
#                 print(listA[i]['name'],':',listA[i]['tel'])
#             else:
#                 print('%s의 전화번호는 저장 되어 있지 않습니다!'%name)
                

#     elif menu == 2:
#             print('리스트 내용','\n',listA[0],'\n',listA[1],'\n',listA[2])
#             break

#     else:
#         print('입력 오류!!!')
		

# listA = []
# #입력받아 딕셔너리로 만든 후 리스트 추가
# for i in range(3):
# 	a= input('이름 : ')
# 	b= input('전화:')
# 	dic={'name':a, 'tel':b}
# 	listA.append(dic)
# 	#list A 에다가 dic를 삽입 또는 추가
# print(listA)
# while True :
# 	menu = int(input('1.검색  2.종료 :')) 
# 	if menu == 1:
# 		name = input('검색할 이름 : ')
# #		for i in range(len(listA)):
# #			if listA[i]['name'] == a:
# #				print(listA[i]['tel'])
# #			else:
# #				print(dic["name"]+'의 전화번호는 저장되어 있지 않습니다!')

# 		for val in listA:#-> for로 일일이 다 돌려봐야 함.
# 			#name = input('검색할 이름 : ')
# 			if val['name'] == a:
# 				print(listA['name']['tel'])
# 			else:
# 				print(dic["name"],"의 전화번호는 저장되어 있지 않습니다!")
				
# 	elif menu == 2:
# 		break
# 		print('리스트 내용')
# 		print(listA)
# 	else:
# 		print('잘못된 번호를 입력함!!!')

# list1=[]
# sum=0

# while True:
	
# 	num=int(input("정수 입력:"))
# 	if num<0 or num>0:
# 		list1.append(num)
# 	else:
# 		print(list1)
# 		print("역순:",end=" ")
# 		for i in range(len(list1)-1,-1,-1):
# 			print(list[i],end=" ")


# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# group = ['A', 'B', 'C', 'D', 'E', 'F']
# name = ['가영', '나은', '다희', '라율']

# all_list = [group[0], name[0:2], group[1:4], name[2], group[4:6], name[3]]
# #[group, name]
# #print(group[0:1], name[6:9], group[1:4], name[7:9], group[4:6], name[8:10])

# #print(group[0:1], name[6:9], group[1:4], name[7:9], group[4:6], name[8:10])
# print(all_list)



# listA=[]
# while True:
# 	num=int(input('정수 입력 : '))
# 	if num==0:
# 		print(listA)
# 		break
# 	listA.append(num)
# print('\n역순 : ',listA[::-1])
	
# a=int(input('\n삽입 정수 : '))
# b=int(input('삽입할 인덱스 : '))
# if b>len(listA):
# 	print('index의 범위에 맞지 않습니다!!')
# else:
# 		listA.insert(b,a)
# 		print(listA)
# c=int(input('삭제할 정수 : '))
# if c in listA:
# 	listA.remove(c)
# else:
# 	print('%d은 존재하지 않습니다!%(c)')
# print(listA)
# print('역순 : ',listA[::-1])
# print('정렬 : ',sorted(listA))



# list1 = [0, 1, 2, 4, 5]

# print('역순 :',end='')
# for i in range(len(list1),0, -1):  
# 	if i-1 == 0:
# 		print(list1[i-1]) 
# 	print(f'{list1[i-1]}, ', end='')



# num_list = [0,2,3,5]

# num_list.reverse() #이렇게 하는 이유는 reverse()는 리스트의 인덱스 순서를 뒤집지만, 직접적으로 바뀐 리스트의 값을 대상 리스트인 num_list에 저장해주지 않아요ㅜㅜ 그래서 변수를 통해 따로 저장을 해야해요!
# print('역순 :', num_list) #요 부분이 문제더라구요...!
# num_list.sort() 
# print('정렬 :', num_list)



# num_list=[]
# while True:
	
# 	num=int(input('정수 입력:'))
	
# 	if num ==0:
# 		break
# 	elif num!=0:
# 		num_list.append(num)
# print(num_list)
# print()

# print('역순 :', end='')
# for i in range(len(num_list)-1,0-1,-1):
# 	print(num_list[i],'',end='')

# num1=int(input('삽입 정수:'))
# idx=int(input('삽입할 인덱스:'))
		
# if len(num_list)<idx:
# 	print('index의 범위에 맞지 않습니다.')
# 	print(num_list)
# else:
# 	num_list.insert(idx,num1)
# 	print(num_list)
			
# delt=input('삭제할 정수 :')
# if delt in num_list:
# 	num_list.remove(delt)
# 	print(num_list)
# # num_list
# print('역순 :', num_list.reverse())
# print('정렬 :', num_list.sort())


# list1=[]
# while True:
# 	add=int(input('정수 입력: '))
# 	if add==0:
# 		break
# 	elif add!=0:
# 		list1.append(add)
# print(list1)
# print()

# print('역순 :', end='') #수정
# for i in range(len(list1), 0, -1):
# 	print(i , end=' ')
# num=input('삽입할 정수 : ')
# idx=int(input('삽입할 인덱스 : '))

# if idx>len(list1):
# 	print('index의 범위에 맞지 않습니다.')
# 	print(list1)
# else:
# 	list1.insert(idx, num)
# 	print(list1)

# det=int(input('삭제할 정수 : '))
# if det in list1:
# 	list1.remove(det)
# 	print(list1)
# else:
# 	print(det+'는 존재하지 않습니다!')
# 	print(list1)
				
# print('역순 :', list1[::-1])
# print('정렬 :', list1.sort())


# num=int(input("출력 줄수 입력:"))

# for i in range(1, num+1): #i는 1부터 num까지의 정수
# 	print('{:(num-1)}') #첫 번째 * 앞의 공백 칸수는 "출력 줄수"보다 1 작은 수이므로 num-1만큼의 공백 입력
# for j in range(1, num+1): #j는 1부터 num까지의 정수
# 	print('*'*(num*2-1)) #각 줄의 * 개수는 (해당 줄 번호*2-1)이므로 그 개수만큼의 * 입력

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