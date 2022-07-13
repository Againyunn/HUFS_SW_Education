result = ''
thisSum = 0
multiple= 9

while thisSum + multiple <100: 
    thisSum += multiple
    result += str(multiple)

    if thisSum + multiple <100:
        result += ' + '

    multiple += 9

result += f' = {thisSum}'
print(result)
