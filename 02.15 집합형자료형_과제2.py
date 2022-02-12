testList = (["3+2", 5, 3], ["6/2", 3, 5], ["10-2", 8, 3], ["2의 3승", 8, 4], ["5-2*2", 1, 5])
correct =0
score=0



for i in range(len(testList)):
    answer = input(f"{testList[i][0]} : ")
    if answer == str(testList[i][1]):
        score += testList[i][2]
        correct += 1

print(f'정답수 : {correct}')
print(f'오답수 : {len(testList)-correct}')
print(f'점 수 : {score}')

