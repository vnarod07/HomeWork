import math
alphabet = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = 0
res = input()
for i in range(len(res)):
    for j in range(52):
        if alphabet[j] == res[i]:
            num += j+1

if num == 1 or num == 2:
        print('It is a prime word.')
        exit()

for k in range(2, math.ceil(math.sqrt(num))+1):
    
    if num % k == 0:
        print('It is not a prime word.')
        break
    else:
        if k ==  math.ceil(math.sqrt(num)):
            print('It is a prime word.')
    
    
            
