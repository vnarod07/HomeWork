import math
M = int(input()) ; N = int(input())
if M == 1 : M = 2

prime = set()
for i in range(M, N+1):
    S=0
    for j in range(2, math.ceil(math.sqrt(i))+1):
        if i%j == 0: S=1
        if i==2 & j==2: S=0
    if S == 0: prime.add(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
