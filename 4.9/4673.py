nagari = set()
output = set(range(1,10001))

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    nagari.add(i)
    
    
output = sorted(list(output - nagari))
for i in output:
    print(i)
