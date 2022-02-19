import score 
# score.py참고

ban =[]
for i in range(5):
    student=[]
    student.append(input('성명 : '))
    student.append(int(input('국어점수 : ')))
    student.append(int(input('영어점수 : ')))
    student.append(int(input('수학점수 : ')))
    ban.append(student)

for i in range(5):
    #2차원 리스트의 각 1차원 리스트에 값 추가

    #total 계산
    ban[i].append(score.total(ban[i]))

    #ave 계산
    ban[i].append(score.ave(ban[i]))

    #grade 계산
    ban[i].append(score.grade(ban[i]))

    #output 출력
    score.output(ban[i])


print('\n2명 성적 비교하여 더 좋은 점수의 학생 찾기')
score.output(ban[2])
score.output(ban[4])
print('성적이 더 좋은 학생')
score.output(score.max_student(ban[2], ban[4]))

print('\n3명 성적 비교하여 더 좋은 점수의 학생 찾기')
score.output(ban[1])
score.output(ban[2])
score.output(ban[3])
print('성적이 더 좋은 학생')
score.output(score.max_student(ban[1], ban[2], ban[3]))