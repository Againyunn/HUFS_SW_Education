#학생 값 입력
student = []

#total
def total(student): #국 영 수 총합
    scoreTotal = student[1] + student[2] + student[3]
    return(scoreTotal)

#ave
def ave(student):
    return(student[4]/3)

#grade
def grade(student):
    if student[5] >= 90:
        return 'A'
    elif student[5] >= 80:
        return 'B'
    elif student[5] >= 70:
        return 'C'
    elif student[5] >= 60:
        return 'D'
    elif student[5] < 60:
        return 'F'

#output
def output(student):
    print(f'{student[0]} : 국어 :{student[1]} 영어 :{student[2]} 수학 :{student[3]} 총점 :{student[4]} 평균 :{student[5]} 학점 :{student[6]}')


#max_student
def max_student(*student):
    if student == None:
        return

    maxScore = student[0][4]
    highScoreStudent = student[0]
    for i in range(len(student)):
        if maxScore < student[i][4]:
            maxScore = student[i][4]
            highScoreStudent = student[i]

    return highScoreStudent