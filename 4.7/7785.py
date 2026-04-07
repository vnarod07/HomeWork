N = int(input())
output = set()
for i in range(N):
    a = input().split()
    if a[1] == 'enter':
        output.add(a[0])
    else:
        output.remove(a[0])

output = sorted(output, reverse=True)

for i in output:        
    print(i)
