def average(kor, eng, math):
    return (kor + eng + math)/3

kor = int(input('국어 점수를 입력하세요: '))
eng = int(input('영어 점수를 입력하세요: '))
math = int(input('수학 점수를 입력하세요: '))

print('국어는 {0}점, 영어는 {1}점, 수학은 {2}점이며, 총 평균은 {3:.2f}점 입니다.'.format(kor, eng, math, average(kor, eng, math)))