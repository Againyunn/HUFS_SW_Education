num = int(input())

if num <= -10 or 10 <= num:
    print("1점입니다.")
elif num <= -7 or 7 <= num:
    print("2점입니다.")
elif num <= -3 or 3 <= num:
    print("3점입니다.")
elif num <= -1 or 1 <= num:
    print("4점입니다.")
elif num == 0:
    print("축하합니다! 5점입니다.")
else:
    print("점수를 출력할 수 없습니다.")
