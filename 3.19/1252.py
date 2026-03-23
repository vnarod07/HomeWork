
a, b = input().split()
if len(a) > len(b):
    b = '0' * (len(a)-len(b))+b
if len(a) < len(b):
    a = '0' * (len(b)-len(a))+a
a=list(a)
output = []

for i in range(len(a)-1, -1, -1):
    if int(a[i]) + int(b[i]) < 2:
        output.append(str(int(a[i]) + int(b[i])))
    elif int(a[i]) + int(b[i]) >= 2:
        if int(a[i]) + int(b[i]) == 2:
          output.append('0')
        else:
          output.append('1')

        if i == 0:
          output.append('1')
        else:
          a[i-1] = str(int(a[i-1])+1)



output.reverse()
output = ''.join(output)
for i in range(len(output)):
  if output[i] == '1':
    print(output[i:])
    break
  elif i == len(output)-1:
    print(0)
