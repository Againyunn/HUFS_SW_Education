with open('students.txt', 'w') as file:
    for i in range(5):
        name = input('이름 입력 : ')
        midterm = input('중간고사 점수 : ')
        final = input('기말고사 점수 : ')

        file.write(f"{name}, {midterm}, {final}\n")
        


