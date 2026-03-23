num = input()
output = []
eightrecord = ['000', '001', '010', '011','100','101','110','111']

def TwoToEight(startindex, len):
    for i in range(0, len+1, 3):
        for j in range(8):
            if eightrecord[j] == num[(startindex+i):(startindex+i+3)]:
                output.append(str(j))
    
if len(num) % 3 == 0:
    TwoToEight(0, len(num))
elif len(num) % 3 == 1 and len(num) != 1:
    output.append('1') 
    TwoToEight(1, len(num)-1)
elif len(num) == 1:
    if num[0] == '0':
        print('0')
        
    else:
        print('1')
elif len(num) % 3 == 2 and len(num) != 2:
    if num[0:2] == '10':
        output.append('2')
    else:
        output.append('3')
    TwoToEight(2, len(num)-2)

else:
    if num[0:2] == '10':
        print('2')
    else:
        print('3') 

output = ''.join(output)

for i in range(len(output)):
  if output[i] != '0':
    print(output[i:])
    break
