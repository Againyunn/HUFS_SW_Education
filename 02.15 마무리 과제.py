answer = input()

total = 0
current = 1

for i in range(len(answer)):    #입력받은 답의 수만큼 반복
    if answer[i] == 'O':    #O인 값을 식별
        total += current
        current += 1
    elif answer[i] == 'X':      #X인 값을 식별
        if current >= 1:    #current를 초기화
            current = 1

print(total)