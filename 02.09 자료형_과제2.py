thisInch = float(input('inch 입력 : '))

thisCm = thisInch * 2.54

print(f'학번 :{"201703262".rjust(20)}')
print(f'성명 :{"Jung Jaeyun".rjust(20)}')
print('==============================')
print("     {0:08.2f} inch".format(thisInch))
print("     {0:08.2f} cm".format(thisCm))
print('==============================')