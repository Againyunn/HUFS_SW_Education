# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def calNums(base, *nums) :
	for i in range(len(nums)):
		total = base
		for j in range(nums[1],nums[i]+1):
			total *= base
		print(f'{base}의 {nums[i]} 제곱 값은 {total}이다.')
	
calNums(5, 1, 2, 3)
calNums(2, 2, 4, 6, 8, 10)


# print('이름 중간 기말 총점 평균 학점')

# f=open('students.txt', 'r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     (name,score1,score2)=line.strip().split(',')
#     s=int(score1)+int(score2)
#     m=s/2
    
   
#     if m >= 90:
#         r='A'
#     elif m >= 80:
#         r='B'
#     elif m >= 70:
#         r='C'
#     elif m >= 60:
#         r='D'
#     else:
#         r='F'
        
    
#     print(' {0}   {1}   {2}   {3}   {4:.2f}   {5}'.format(name, score1, score2, s, m, r))
# f.close()

# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean

# #기말고사에 binary() 재귀함수 나오지 않습니다!!!!!
# print('이름   중간   기말   총점   평균   학점')

# file = open('students.txt','r')
# while True:
#     line=file.readline()
#     if not line:
#         break
#     (name, mid, fin)=line.strip().split(',')
#     ave = (int(mid) + int(fin))%2
#     sum1 = int(mid) +int(fin)

#     if ave>=90:
#         gra='A'
#     elif 80<=ave<90:
#         gra='B'
#     elif 70<=ave<80:
#         # gra='C'
#     elif 60<=ave<70:
#         gra='D'
#     elif ave<60:
#         gra='F'
#     print('ff')
#     print('{0}  %s    %s  %d  %5.1f  %s' .format(name,mid,fin,sum1,ave,gra))   
        


# # kor = 1


# # # print(f'평균은 {kor:.2f}')

# # print('name   mid  final  total  average  result')
# # file=open('students.txt','r')  

# # while True:
# # 	line=file.readline()
# # 	if not line:
# # 		break
		
# # 	(name,mid,final)=line.strip().split(',')
# # 	total=int(mid)+int(final)
# # 	average=total/2
# # 	if total>=90:
# # 		result='A'
# # 	if 90>total>=80:
# # 		result='B'
# # 	if 80>total>=70:
# # 		result='C'
# # 	if 70>total>=60:
# # 		result='D'
# # 	if total<60:
# # 		result='F'
	
# # 	print('%-8s %4s %4s %5.2% %10s' %(name,mid,final,total,average,result))
# # file.close() # 아직 txt 파일 내부에서 출력할 값이 남아있는데 파일을 while반복문 안에서 닫았기 때문에 더이상 값을 불러오지 못하는 것 같아요. 이부분을 while반복문 바깥으로 빼 보세요~
	



# # # line = '사 람 들' #이 살아가는 게'
# # # (name,mid,fin)=line.strip().split(' ')
# # # print(name)
# # # print(mid)
# # # print(fin)
# # # -*- coding: utf-8 -*-
# # # UTF-8 encoding when using korean

# # # #기말고사에 binary() 재귀함수 나오지 않습니다!!!!!
# # # print('이름  중간  기말  총점  평균  학점')
# # # file=open('students.txt','r')
# # # while True:
# # #     line=file.readline()
# # #     if not line:
# # #         break
    
# # #     (name,mid,fin)=line.strip().split(',')
# # #     mid=int(mid)
# # #     fin=int(fin)
# # #     total=mid+fin
# # #     average=total/2

# # #     if average >= 90:
# # #         grade = 'A'
# # #     elif average >= 80:
# # #         grade = 'B'
# # #     elif average >= 70:
# # #         grade = 'C'
# # #     elif average >= 60:
# # #         grade = 'D'
# # #     else:
# # #         grade = 'F'
	
# # #     print('%s   %d  %d  %d  %f  %s'%(name,mid,fin,total,average,grade))


# # # # -*- coding: utf-8 -*-
# # # # UTF-8 encoding when using korean
# # # file=open('student.txt', 'r')
# # # data=file.readlines()

# # # print('이름   중간   기말   총점   평균   학점')

# # # for i in range(len(data)):
# # # 	print(data, end='')
# # # 	total=int(data[i][1])+int(data[i][2])
# # # 	average=total/2
# # # 	if average>=90:
# # # 		grade='A'
# # # 	elif averge>=80:
# # # 		grade='B'
# # # 	elif average>=70:
# # # 		grade='C'
# # # 	elif average>=60:
# # # 		grade='D'
# # # 	else:
# # # 		grade='F'
	
# # # 	print('''i[0]   i[1]   i[2]   total  average  grade''')


# # # file.close()

# # # # -*- coding: utf-8 -*-
# # # # UTF-8 encoding when using korean

# # # #기말고사에 binary() 재귀함수 나오지 않습니다!!!!!
# # # print('이름 중간 기말 총점 평균 학점')
# # # # with open('students.txt','w') as s:
# # # #     for i in range(1):
# # # #         name=input('이름 입력: ')
# # # #         score1=int(input('중간고사 점수: '))
# # # #         score2=int(input('기말고사 점수: '))
# # # #         s.write('{},{},{}\n'.format(name,score1,score2))



# # # file=open('students.txt', 'r')
# # # while True:
# # #     line=file.readline()
# # #     if not line:
# # #         break
# # #     (name,score1,score2)=line.strip().split(',')
# # #     s=int(score1)+int(score2)
# # #     m=s/2
    
   
# # #     if m >= 90:
# # #         r='A'
# # #     elif m >= 80:
# # #         r='B'
# # #     elif m >= 70:
# # #         r='C'
# # #     elif m >= 60:
# # #         r='D'
# # #     else:
# # #         r='F'
# # #     print('%-8s %4s %4s %4d %5.1f %10s'%(name,score2,score2,s,m,r))

# # # file.close()



# # # # -*- coding: utf-8 -*-
# # # # UTF-8 encoding when using korean

# # # #기말고사에 binary() 재귀함수 나오지 않습니다!!!!!
# # # print('이름  중간  기말  총점  평균  학점')
# # # file=open('students.txt', 'r')
# # # while True:
# # #     ss = file.readline()

# # #     if not ss :
# # #         break

# # #     name, mid, fnl = ss.strip().split(',')
# # #     mid = int(mid)
# # #     fnl = int(fnl)
# # #     sum = mid+fnl
# # #     mean = (mid+fnl)/2

# # #     if mean >= 90:
# # #         re = 'A'
# # #     elif mean >= 80:
# # #         re = 'B'
# # #     elif mean >= 70:
# # #         re = 'C'
# # #     elif mean >= 60:
# # #         re = 'D'
# # #     else:
# # #         re = 'F'
# # #     print('{:2s}{:4d}  {:4d} {:4d}   {:4.1f}   {:4s}'.format(name, mid, fnl, sum, mean, re))
# # # file.close()
        

# # #     mid = int(mid)
# # #     fnl = int(fnl)
# # #     mean = (mid+fnl)/2

# # #     if mean >= 90:
# # #         re = 'A'
# # #     elif mean >= 80:
# # #         re = 'B'
# # #     elif mean >= 70:
# # #         re = 'C'
# # #     elif mean >= 60:
# # #         re = 'D'
# # #     else:
# # #         re = 'F'
# # #     print('{:2s}{:4d}  {:4d}  {:4.1f}   {:4s}'.format(name, mid, fnl, mean, re))
# # # file.close()
        

# # # with open('students.txt', 'w')as file:
# # #     for i in range(5):
# # #         name=input('이름 입력:')
# # #         mid=input('중간고사 점수:')
# # #         fnl=input('기말고사 점수:')

# # #         file.write('{}, {}, {} \n'.format(name, mid, fnl))

# # # with open('student.txt', 'w') as file:
# # # 	for i in range(5):
# # # 		name=input('이름 입력:')
# # # 		midterm=input('중간고사 점수:')
# # # 		final=input('기말고사 점수:')
# # # 		file.write('{}, {}, {}\n'.format(name, midterm, final))

# # # phones = {'model':'iPhone11', 'manufacturer':'Appple', 'year':'2019'}

# # # print(phones['year'])
# # # # print(phones.get('year'))

# # # phones.clear()
# # # print(phones)
# # # # del phones[{'model','manufacturer','year'}]

# # # # -*- coding: utf-8 -*-
# # # # UTF-8 encoding when using korean

# # # def binary(number):
# # # 	global count
# # # 	count += 1 #함수 호출 획수 1 증가
# # # 	if number == 1 or number == 0: #재귀함수를 끝낼 조건
	
# # # 		v1=number//2  #몫을 저장
# # # 		v2=number%2   #나머지 저장
# # # 		listA.insert(0, v2) #나머지를 리스트의 인덱스 0 에 삽입
# # # 		return binary(v1) #몫으로 다시 binary 함수 호출


# # # count = 0  #binary() 함수 호출 횟수 저장 변수
# # # listA=[]  #이진수로 변환된 값 저장할 리스트
# # # while True:
# # # 	num = int(input('양의 정수 입력(음수입력시 종료) :'))

# # # 	if num <0 :
# # # 		break
		
# # # 	else:
# # # 		listA.clear() #listA 리스트의 모든 원소 지움
# # # 		count = 0 #count 변수 다시 0으로 지정
# # # 		binary(num) #binary 함수 호출
# # # 		for i in listA:
# # # 			str1=''
# # # 			str1+=str(i)
# # # 			print(str1)
# # # 	print(listA)
# # # 	print(num, '의 이진수 :', listA, end=' ')
# # # 	#리스트의 저장된 값을 앞에서 부터 하나씩 읽어서 보여줌
# # # 	print('binary() 함수 반복횟수 : ', count)
# # # 	print()
	

# # # def binary(number):
# # # 	global count
# # # 	count+=1#함수 호출 획수 1 증가
# # # 	v2=number%2
# # # 	v1=number//2  #몫을 저장
# # # 	if v1 ==0:	#재귀함수를 끝낼 조건
# # # 		v2=number%2
# # # 		return #일단 이쪽에 return은 해주어야 해요! return이 없으면 무한 반복해서ㅜㅜ 아 그렇군요...
# # # 	# 일단 지금 상황 파악을 위해 한번 코드 돌려볼게요!넵
# # # 	   #나머지 저장
# # # 	listA.insert(0, v2)#나머지를 리스트의 인덱스 0 에 삽입
# # # 	return binary(v1)#몫으로 다시 binary 함수 호출
# # # # 지금 확인했을 때 첫번째 연산을 놓치는 것 같아요! 그 외에는 전반적으로 잘 답는 것 같은데ㅜ 그래서 이 부분만 수정해보면 될 것 같아요!
# # # # 아까 에러가 났던 점은 재귀가 안 멈추는 것이었죠? 그 뭐냐29열에 함수 호출하는 부분하고 9열에 

# # # # 안녕하세요 조교입니다. 재귀호출이 끝나 지않는다던데ㅜㅜ 어떤 문제인가요? 교수님께서 몫이 0이 되면 멈춘다고 하셔서 몫이 0일때 리턴값을 주지 않는 것으로 해놓았는데 v1이 오류가 났네요. 한번 확인해볼게요! 
# # # count=0  #binary() 함수 호출 횟수 저장 변수
# # # listA=[]  #이진수로 변환된 값 저장할 리스트 
# # # while True:
# # # 	num = int(input('양의 정수 입력(음수입력시 종료) :'))
# # # 	if num <0 :
# # # 		break
		
# # # 	else:
# # # 		listA.clear()#listA 리스트의 모든 원소 지움
# # # 		count=0#count 변수 다시 0으로 지정
# # # 		binary(num)#binary 함수 호출
# # # 	print(num, '의 이진수 :', end=' ')
# # # 	print(listA)
# # # 	#리스트의 저장된 값을 앞에서 부터 하나씩 읽어서 보여줌
# # # 	print('binary() 함수 반복회수 :', count )
# # # 	print()

# # # # -*- coding: utf-8 -*-
# # # # UTF-8 encoding when using korean

# # # def binary(number):
# # # 	global count
# # # 	count+=1   #함수 호출 획수 1 증가
# # # 	if number//2==0:	#재귀함수를 끝낼 조건
# # # 		v2=number%2
# # # 		listA.insert(0,v2)
# # # 		return listA
# # # 	else:
# # # 		v1=number//2  #몫을 저장
# # # 		v2=number%2   #나머지 저장
# # # 		listA.insert(0,v2)	#나머지를 리스트의 인덱스 0 에 삽입
# # # 		return binary(v1)	#몫으로 다시 binary 함수 호출

# # # count=0  #binary() 함수 호출 횟수 저장 변수
# # # listA=[]  #이진수로 변환된 값 저장할 리스트
# # # while True:
# # # 	num = int(input('양의 정수 입력(음수입력시 종료) : '))
# # # 	if num <0 :
# # # 		break
# # # 	else:
# # # 		listA.clear()	#listA 리스트의 모든 원소 지움
# # # 		count=0   #count 변수 다시 0으로 지정
# # # 		f=binary(num)	#binary 함수 호출
		
# # # 		print(num, '의 이진수 : ', end=' ')
# # # 		for ele in f:
# # # 			print(ele, end='')   #리스트의 저장된 값을 앞에서 부터 하나씩 읽어서 보여줌
# # # 		print(end='  ')
# # # 		print('binary 함수 호출횟수 :', count )
# # # 		print()
	



# # # def binarty(num):
# # #     global count
# # #     count=0
    
# # #     global listb
# # #     listb=[]
# # #     # listb.insert(0,num%2)
# # #     num2=num%2
# # #     if num2 != 1:
# # #         binarty(num2)
# # #         listb.insert(0,num2%2)
# # #         count+=1
        
# # #     elif num2 == 1:
# # #         listb.insert(0,1)
# # #         return listb

# # # while True:
# # #     num=int(input('양의 정수 입력(음수 입력시 종료): '))
# # #     if num >= 0:
# # #         binarty(num)
# # #     else:
# # #         break
# # #     print(f'{num}의 이진수:',listb,' ','binary() 함수 반복횟수: ',count)


# # # 안녕하세요 조교입니다.
# # # 전체적으로 과제 수행할 때 도움이 될만한 부분을 정리해서 안내드려요.
# # # 1. def find_max(*num): 함수를 통해 입력받는 인자(num이 0개, 1개, ... 5개)의 수가 바뀔 때에도 입력받는 인자들 중 가장 큰 값을 return하도록 함수를 작성
# # # 지금 코드는 nums의 길이만 비교하고 nums의 값들을 서로 비교하지 못해요. 
# # # 그러니, for문과 if문을 활용해서 입력받은 nums의 값들을 모두 반복하며 각각 비교해서 가장 큰 값으로 max를 덮어씌우는 방식으로 코드를 작성해주세요.

# # # 2. 숫자 5개를 입력
# # # for문으로 입력을 받아도 되지만 구현이 힘들다면, num1 = input('정수 입력 : ')이런 방식으로 num1~num5까지 입력받아도 될 거에요.

# # # 3. print('find_max()=', find_max())
# # # print('find_max(숫자1)=', find_max(숫자1))
# # # print('find_max(숫자1, 숫자2)=', find_max(숫자1, 숫자2))  → find_max(num1, num2) 하면 num1과 num2를 find_max 함수에 인자로 입력합니다.
# # # ..

# # # 이런식으로 find_max라는 함수에 입력받는 숫자의 수를 점차 늘려가며 값을 출력하면 되는 문제에요!

# # # 전체적인 과제 수행 방법은 다음과 같아요.

# # # 1. def find_max(*num): 함수를 통해 입력받는 인자(num이 0개, 1개, ... 5개)의 수가 바뀔 때에도 입력받는 인자들 중 가장 큰 값을 return하도록 함수를 작성

# # # 2. 숫자 5개를 입력

# # # 3. print('find_max()=', find_max())

# # # print('find_max(숫자1)=', find_max(숫자1))

# # # print('find_max(숫자1, 숫자2)=', find_max(숫자1, 숫자2))

# # # ..

# # # 이런식으로 find_max라는 함수에 입력받는 숫자의 수를 점차 늘려가며 값을 출력하면 되는 문제에요!

# # # 추가적으로 현재 작성하신 코드의 몇 가지 보이는 문제를 알려드리면,

# # # 1. 함수 안에서는 list1 대신 입력받은 인자인 'num'을 활용해야 에러가 발생하지 않을 거에요.

# # # for j in range(len(num)): 이런식으로 지금 작성하신 코드에서 수정하시면 될 거에요.

# # # 2. add=input() 코드는 add에 str형태의 데이터를 저장해요! → int형 데이터로 바꿔주셔야 크기를 비교할 수 있을 거에요.

# # # 3. max=0 을 함수 안에서 작성해주세요.

# # # 지금처럼 코드를 작성할 경우에는 max라는 변수의 범위가 함수 안에 까지 미치지 못해요ㅜㅜ

# # # global이라는 전역변수를 사용할 수도 있겠지만, 이는 지금 공부 범위에서 벗어났을 것 같아 추천드리지 않구

# # # 함수 안에 max = 0을 넣는 방법 추천드려요:)

# # # def find_max(*num):
# # # 	max = num[0]
# # # 	for j in range(len(list1)):
# # # 		if max<list1[j]:
# # # 			max=list1[j]
			
# # # 	return max	
	
# # # max=0	
# # # list1=[]

# # # for i in range(5):
# # # 	add=int(input())
# # # 	list1.append(add)
	
# # # find_max(list1)
# # # print(find_max)


# # # def find_max(*nums):
# # # 	if len(nums) <= 0:
# # # 		max = 0
# # # 	#nums 에 값이 하나도 없을때  
# # # 	#max에 0을 저장
# # # 	else:
# # # 		max = nums[0]
# # # 		#가변 변수중 가장 처음 변수를 max에 저장

# # # 	for i in range(len(nums)):
# # # 		if max < nums[i]:
# # # 			max = nums[i]
# # # 			#nums 에서 원소를 하나씩 꺼내옴
# # # 	   #꺼내온 원소가 max 보다 크면 그 값을 max 로 지정
		
# # # 	return max


# # # n1=int(input('정수 1 : '))
# # # n2=int(input('정수 2 : '))
# # # n3=int(input('정수 3 : '))
# # # n4=int(input('정수 4 : '))
# # # n5=int(input('정수 5 : '))

# # # print('find_max()=', find_max())
# # # print('find_max(n1)=', find_max(n1))
# # # print('find_max(n1, n2)=', find_max(n1, n2))
# # # print('find_max(n1, n2, n3)=', find_max(n1, n2, n3))
# # # print('find_max(n1, n2, n3, n4)=', find_max(n1, n2, n3, n4))
# # # print('find_max(n1, n2, n3, n4, n5)=', find_max(n1, n2, n3, n4, n5))



# # # def find_max(*nums):
# # #     max = 0
# # #     for i in range (len(nums)):
# # #         if nums != ():
# # #             if max < nums[i]:
# # #                 max = nums[i]
# # #         else:
# # #             max = 0
# # #     return max

# # # num = [0,0,0,0,0]
# # # for i in range(5):
# # # 	num[i] = int(input('정수 입력: '))

# # # print('find_max()','=',find_max())
# # # print('find_max(num1)','=',find_max(num[0]))
# # # print('find_max(num1,num2)','=',find_max(num[0],num[1]))
# # # print('find_max(num1,num2,num3)','=',find_max(num[0],num[1],num[2]))
# # # print('find_max(num1,num2,num3,num4)','=',find_max(num[0],num[1],num[2], num[3]))
# # # print('find_max(num1,num2,num3,num4,num5)','=',find_max(num[0],num[1],num[2], num[3], num[4]))


# # # 지금 발생한 문제는 break를 else에 걸어서, 한번이라도 검색이 되지 않으면 반복을 종료하기 때문에 첫번째 입력받은 name이 아닌, 다른 name을 입력받으면 정상적으로 출력이 안되는 상태에요:)
# # # 현 코드의 else문의 break를 삭제하면 2가지 문제가 잠재적으로 발생할거에요.
# # # 문제1. listA에 저장된 name을 검색했는데도 '{name}의 전화번호는 저장되어 있지 않습니다!' 오류가 계속 출력되는 상황
# # # 문제2. '{name}의 전화번호는 저장되어 있지 않습니다!' 오류는 한번만 출력되면 되는데, 2번이상 출력되는 상황
# # # 여기서 문제1의 원인은 if listA[i]['name'] == name:의 조건이 True인 값을 찾아도 반복문이 끝나지 않고 다음 인덱스까지 탐색하기 때문에 발생해요. 그래서 break를 통해 조건을 찾았다면 반복문을 탈출하게 만들면 될 거에요.
# # # 문제2의 원인은 else: 이 조건은 name이 listA에 없는 모든 경우에 오류 문장을 출력하라는 의미가 되어요.
# # # 그래서 if의 조건을 "반복을 다 끝냈을 때(i가 listA의 마지막 원소 값일 때)" 로 바꿔주고, '{name}의 전화번호는 저장되어 있지 않습니다!' 오류를 출력하면 될 거에요.




# # # 인덱스는 []로, 튜플은 ()로 둘러싸인 자료형이잖아요?
# # # 그래서 교수님께서 과제에 적어주신 것 같은 내용을 담은 튜플을 만들고, 물음에 따른 답을 출력하라는 의미에요.

# # # * 과제에서 요구하는 튜플 선언
# # # 튜플이름 = (["3+2", 5, 3], ["6/2", 3, 5], ["10-2", 8, 3], ["2의 3승", 8, 4], ["5-2*2", 1, 5])   #튜플이름 이라는 변수에 ["3+2", 5, 3], ["6/2", 3, 5], ["10-2", 8, 3], ["2의 3승", 8, 4], ["5-2*2", 1, 5] 의 원소가 튜플 자료형으로 담겨요!

# # # 여기서 예를 들어 ["3+2", 5, 3]를 뜯어보면,
# # # "3+2" : 문제(질문)
# # # 5       : 정답
# # # 3       : 배점
# # # 이런 식으로 다른 [ ] 안의 값들도 이해하고 각 질문 별로 입력받은 답을 "튜플이름"에 저장된 값과 비교해서 맞으면 배점만큼 점수를 누적하는 방식으로 과제를 풀면될거에요!


# # # 불필요한 for문 연산으로 인해 지금 문제가 생겼을 것 같아요

# # # * 수정해야 할 코드
# # # for j in range(len(t)):  #반복문을 삭제
# # #     if ans==t[j][1]:  # 각 값을 i로 변경
# # #         sum+=t[j][2]
# # #         correct+=1
# # #     elif ans!=t[j][1]:
# # #         ans+=0
# # #         correct+=0
# # # 지금은 바깥의 for문의 증감값(변화하는 값)인 i가 각 문제들을 가리키고 있는데, 두번째  for문을 한번 더 돌아서 j라는 인덱스로 모든 리스트의 값과 한번 더 비교하니까 
# # # 정상적인 정답을 비교하지 못해서, 점수를 제대로 기록하지 못하고 있어요.
# # # 그래서 for j in range(len(t)): 반복문을 삭제하고 아래 코드들의 j를 i로 바꾸면 문제가 해결될 거에요.



# # # listA=[]

# # # #입력받아 딕셔너리로 만든후 리스트 추가
# # # for i in range(3):
# # # 	a=input('이름 :')   
# # # 	b=input('전화 :')
# # # 	dic={'name':a, 'tel':b}
# # # 	# listA.append(dic)
# # # listA.extend(dic)
# # # print(listA)
# # # #listA 에다가 dic 를 삽입 또는 추가
	
  
# # # 	#[  {'name':'홍길동', 'tel':'123-432-4332'},
# # # 	#   {'name':'김철수', 'tel':'123-6789-3333'} 
# # # 	#  {.....}
# # # 	#]
	
# # # while True:
# # # 	menu = int(input('1:검색  2:종료 : '))
# # # 	if menu==1:
# # # 		name=input('검색할 이름 : ')
# # # 		for i in range(len(listA)):
# # # 			if listA[i]['name'] == name:
# # # 				print(listA[i]['tel'])
# # # 				break #break 추가
# # # 			elif i == len(listA) - 1:#listA[i][2]: #if조건문으로 바꾸고 조건을 새롭게 설정(i == 마지막 인덱스 번호 )
# # # 				print('%s의 전화번호는 저장되어 있지 않습니다!'%(name))
				
# # # 작성하신 코드를 확인했는데, 아마 2가지 문제로 인해서 질문하신 상황이 발생한 것 같아요.
# # # 문제1. listA에 저장된 name을 검색했는데도 '{name}의 전화번호는 저장되어 있지 않습니다!' 오류가 계속 출력되는 상황
# # # 문제2. '{name}의 전화번호는 저장되어 있지 않습니다!' 오류는 한번만 출력되면 되는데, 2번이상 출력되는 상황
# # # 여기서 문제1의 원인은 if listA[i]['name'] ==name:의 조건이 True인 값을 찾아도 반복문이 끝나지 않고 다음 인덱스까지 탐색하기 때문에 발생해요. 그래서 break를 통해 조건을 찾았다면 반복문을 탈출하게 만들면 될 거에요.
# # # 문제2의 원인은 else: 이 조건은 name이 listA에 없는 모든 경우에 오류 문장을 출력하라는 의미가 되어요.
# # # 그래서 if의 조건을 "반복을 다 끝냈을 때(i가 listA의 마지막 원소 값일 때)" 로 바꿔주고, '{name}의 전화번호는 저장되어 있지 않습니다!' 오류를 출력하면 될 거에요.

# # 	# 	#for val in listA:
# # 	# 	    #if val['name'] ==name
# # 	# 		      #print(val['tel'])
# # 	# elif menu ==2:
# # 	# 	break
# # 	# else:
# # 	# 	print('잘못된 번호를 입력함!!!')



# # # listA = []

# # # for i in range(3):
# # #     a = input('이름 : ')
# # #     b = input('전화 : ')
# # #     dic = {'name':a, 'tel':b}
# # #     listA.append(dic)

# # # print(listA)
# # # while True:
# # #     menu = int(input('1: 검색 2: 종료 '))
# # #     if menu == 1:
# # #         name=input('검색할 이름 : ')
# # #         for i in range(len(listA)):
# # #             if listA[i]['name'] == name:
# # #                 print(listA[i]['name'],':',listA[i]['tel'])
# # #             else:
# # #                 print('%s의 전화번호는 저장 되어 있지 않습니다!'%name)
                

# # #     elif menu == 2:
# # #             print('리스트 내용','\n',listA[0],'\n',listA[1],'\n',listA[2])
# # #             break

# # #     else:
# # #         print('입력 오류!!!')
		

# # # listA = []
# # # #입력받아 딕셔너리로 만든 후 리스트 추가
# # # for i in range(3):
# # # 	a= input('이름 : ')
# # # 	b= input('전화:')
# # # 	dic={'name':a, 'tel':b}
# # # 	listA.append(dic)
# # # 	#list A 에다가 dic를 삽입 또는 추가
# # # print(listA)
# # # while True :
# # # 	menu = int(input('1.검색  2.종료 :')) 
# # # 	if menu == 1:
# # # 		name = input('검색할 이름 : ')
# # # #		for i in range(len(listA)):
# # # #			if listA[i]['name'] == a:
# # # #				print(listA[i]['tel'])
# # # #			else:
# # # #				print(dic["name"]+'의 전화번호는 저장되어 있지 않습니다!')

# # # 		for val in listA:#-> for로 일일이 다 돌려봐야 함.
# # # 			#name = input('검색할 이름 : ')
# # # 			if val['name'] == a:
# # # 				print(listA['name']['tel'])
# # # 			else:
# # # 				print(dic["name"],"의 전화번호는 저장되어 있지 않습니다!")
				
# # # 	elif menu == 2:
# # # 		break
# # # 		print('리스트 내용')
# # # 		print(listA)
# # # 	else:
# # # 		print('잘못된 번호를 입력함!!!')

# # # list1=[]
# # # sum=0

# # # while True:
	
# # # 	num=int(input("정수 입력:"))
# # # 	if num<0 or num>0:
# # # 		list1.append(num)
# # # 	else:
# # # 		print(list1)
# # # 		print("역순:",end=" ")
# # # 		for i in range(len(list1)-1,-1,-1):
# # # 			print(list[i],end=" ")


# # # # -*- coding: utf-8 -*-
# # # # UTF-8 encoding when using korean
# # # group = ['A', 'B', 'C', 'D', 'E', 'F']
# # # name = ['가영', '나은', '다희', '라율']

# # # all_list = [group[0], name[0:2], group[1:4], name[2], group[4:6], name[3]]
# # # #[group, name]
# # # #print(group[0:1], name[6:9], group[1:4], name[7:9], group[4:6], name[8:10])

# # # #print(group[0:1], name[6:9], group[1:4], name[7:9], group[4:6], name[8:10])
# # # print(all_list)



# # # listA=[]
# # # while True:
# # # 	num=int(input('정수 입력 : '))
# # # 	if num==0:
# # # 		print(listA)
# # # 		break
# # # 	listA.append(num)
# # # print('\n역순 : ',listA[::-1])
	
# # # a=int(input('\n삽입 정수 : '))
# # # b=int(input('삽입할 인덱스 : '))
# # # if b>len(listA):
# # # 	print('index의 범위에 맞지 않습니다!!')
# # # else:
# # # 		listA.insert(b,a)
# # # 		print(listA)
# # # c=int(input('삭제할 정수 : '))
# # # if c in listA:
# # # 	listA.remove(c)
# # # else:
# # # 	print('%d은 존재하지 않습니다!%(c)')
# # # print(listA)
# # # print('역순 : ',listA[::-1])
# # # print('정렬 : ',sorted(listA))



# # # list1 = [0, 1, 2, 4, 5]

# # # print('역순 :',end='')
# # # for i in range(len(list1),0, -1):  
# # # 	if i-1 == 0:
# # # 		print(list1[i-1]) 
# # # 	print(f'{list1[i-1]}, ', end='')



# # # num_list = [0,2,3,5]

# # # num_list.reverse() #이렇게 하는 이유는 reverse()는 리스트의 인덱스 순서를 뒤집지만, 직접적으로 바뀐 리스트의 값을 대상 리스트인 num_list에 저장해주지 않아요ㅜㅜ 그래서 변수를 통해 따로 저장을 해야해요!
# # # print('역순 :', num_list) #요 부분이 문제더라구요...!
# # # num_list.sort() 
# # # print('정렬 :', num_list)



# # # num_list=[]
# # # while True:
	
# # # 	num=int(input('정수 입력:'))
	
# # # 	if num ==0:
# # # 		break
# # # 	elif num!=0:
# # # 		num_list.append(num)
# # # print(num_list)
# # # print()

# # # print('역순 :', end='')
# # # for i in range(len(num_list)-1,0-1,-1):
# # # 	print(num_list[i],'',end='')

# # # num1=int(input('삽입 정수:'))
# # # idx=int(input('삽입할 인덱스:'))
		
# # # if len(num_list)<idx:
# # # 	print('index의 범위에 맞지 않습니다.')
# # # 	print(num_list)
# # # else:
# # # 	num_list.insert(idx,num1)
# # # 	print(num_list)
			
# # # delt=input('삭제할 정수 :')
# # # if delt in num_list:
# # # 	num_list.remove(delt)
# # # 	print(num_list)
# # # # num_list
# # # print('역순 :', num_list.reverse())
# # # print('정렬 :', num_list.sort())


# # # list1=[]
# # # while True:
# # # 	add=int(input('정수 입력: '))
# # # 	if add==0:
# # # 		break
# # # 	elif add!=0:
# # # 		list1.append(add)
# # # print(list1)
# # # print()

# # # print('역순 :', end='') #수정
# # # for i in range(len(list1), 0, -1):
# # # 	print(i , end=' ')
# # # num=input('삽입할 정수 : ')
# # # idx=int(input('삽입할 인덱스 : '))

# # # if idx>len(list1):
# # # 	print('index의 범위에 맞지 않습니다.')
# # # 	print(list1)
# # # else:
# # # 	list1.insert(idx, num)
# # # 	print(list1)

# # # det=int(input('삭제할 정수 : '))
# # # if det in list1:
# # # 	list1.remove(det)
# # # 	print(list1)
# # # else:
# # # 	print(det+'는 존재하지 않습니다!')
# # # 	print(list1)
				
# # # print('역순 :', list1[::-1])
# # # print('정렬 :', list1.sort())


# # # num=int(input("출력 줄수 입력:"))

# # # for i in range(1, num+1): #i는 1부터 num까지의 정수
# # # 	print('{:(num-1)}') #첫 번째 * 앞의 공백 칸수는 "출력 줄수"보다 1 작은 수이므로 num-1만큼의 공백 입력
# # # for j in range(1, num+1): #j는 1부터 num까지의 정수
# # # 	print('*'*(num*2-1)) #각 줄의 * 개수는 (해당 줄 번호*2-1)이므로 그 개수만큼의 * 입력

# # # num = int(input())

# # # if num<=0:
# # # 	print('자연수가 아닙니다.')
# # # elif num%2==1:
# # # 	print('입력한 수 %d는 홀수입니다.'%num)
# # # elif num%2==0:
# # # 	print('입력한 수 %d는 짝수입니다.'%num)

# # # n = int(input("출력 줄수 입력 : "))
# # # for i in range(1,n+1):
# # # 	for j in range(1,n+1-i):
# # # 		print(" ", end="")
# # # 	for j in range(2*i-1):
# # # 		print("*", end="")
# # # 	print()
# # # num=int(input('출력 줄수 입력 : '))
# # # for i in range(1,num+1):
# # # 	for j in range(1,num+1-i):
# # # 		print(' ',end='')
# # # 	for j in range(1,i+1):
# # # 		print('*',end='')
# # # 	print()


# # # sum=0
# # # i=9
# # # while sum <=100:
# # #     sum+=i
# # #     if sum + i <100:
# # #         print(i,'+',end='')
# # #         i += 9
# # #     else:
# # #         print(i,'=',end='')
# # #         break
    
# # # print(sum)


# # # sum=0
# # # i=9
# # # while True:
# # # 	sum+=i
# # # 	if sum + i < 100:
# # # 		print(i, '+', end=' ')
# # # 		i+=9
# # # 	else:
# # # 		print(i, '=', end=' ')
# # # 		break

# # # print(sum)