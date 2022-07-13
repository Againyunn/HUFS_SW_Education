file = open("students.txt", "r")

print(" 이름\t중간\t기말\t총점\t평균\t학점")
while True:
    line = file.readline()
    if not line:
        break
    
    (name, midterm, final) = line.strip().split(',')
    sumScore = int(midterm) + int(final)
    average = (sumScore)/2


    if average >= 90:
        score = 'A'
    elif 90 > average >= 80:
        score = 'B'
    elif 80 > average >= 70:
        score = 'C'
    elif 70 > average >= 60:
        score = 'D'
    else:
        score = 'F'
    
    print(f'{name}\t{midterm}\t{final}\t{sumScore}\t{average}\t{score}')

file.close()