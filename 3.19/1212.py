EightToTwo = ['000', '001', '010', '011', '100', '101', '110', '111']
output = []
res = input()
if 0 <= int(res[0]) <= 1:
    output.append(EightToTwo[int(res[0])][2])
elif 2<=int(res[0])<=3:
    output.append(EightToTwo[int(res[0])][1:3])
else:
    output.append(EightToTwo[int(res[0])])
res = res[1:]
j=0

for i in res:
    output.append(EightToTwo[int(res[j])])
    j += 1
print(int(''.join(output)))
