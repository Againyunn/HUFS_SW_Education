num1 = int(input('정수 입력 : '))
num2 = int(input('정수 입력 : '))
num3 = int(input('정수 입력 : '))
num4 = int(input('정수 입력 : '))
num5 = int(input('정수 입력 : '))

def find_max(*args):
    maxNum = 0
    if len(args) == 0:
        return maxNum

    maxNum = args[0]
    for i in range(len(args)):
        for j in range(i,len(args)):
            if maxNum < args[j]:
                maxNum = args[j]
            
    return maxNum

print(f'find_max()={find_max()}')
print(f'find_max({num1})={find_max(num1)}')
print(f'find_max({num1}, {num2})={find_max(num1, num2)}')
print(f'find_max({num1}, {num2}, {num3})={find_max(num1, num2, num3)}')
print(f'find_max({num1}, {num2}, {num3}, {num4})={find_max(num1, num2, num3, num4)}')
print(f'find_max({num1}, {num2}, {num3}, {num4}, {num5})={find_max(num1, num2, num3, num4, num5)}')