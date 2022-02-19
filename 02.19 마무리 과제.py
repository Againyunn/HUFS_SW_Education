# f = open('data/about_python.txt','r')
# sentences = []
# i=0

# while True:
# 	data = f.readline()
# 	if not data:
# 		break
# 	else:
# 		numbering = ("%d번 문장" %(i+1))
# 		data = numbering + data
# 		sentences.append(data)
# 		i += 1
# f.close()

# f = open('data/about_python.txt','r')
# for data in sentences:
# 	print(data, end="")
# f.close()

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

f = open('data/about_python.txt', 'r') 
sentences = []
i=1

while True:
	data = f.readline()
	if not data:
		break
	else:
		numbering = f'{i}번 문장'
		data = numbering+data
		sentences.append(data)
		i+=1
f.close()

f = open('data/about_python.txt', 'w')
for j in range(len(sentences)):
	f.write(sentences[j])
f.close()

f = open('data/about_python.txt','r')
print(f.read())
f.close()