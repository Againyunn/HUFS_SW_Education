S1 = {1, 3}
S2 = {2, 3}
num_list = [1, 3, 4, 5]

print(S1 & S2)
# print(S1.intersection(S2))

print(S1 - S2)
print(S1.difference(S2))

S1.update('hufs')
S1.update(num_list)
print(S1)
