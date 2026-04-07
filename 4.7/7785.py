N = int(input())
output = []
for i in range(N):
    a = input().split()
    if a[1] == 'enter':
        output.append(a[0])
    else:
        output.remove(a[0])

output.sort()

for i in output:        
    print(i)
