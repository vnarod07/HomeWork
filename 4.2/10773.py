N = int(input())
output = 0 ; memory = []
for i in range(N):
    a = int(input())
    if a == 0: del memory[-1]
    else: memory.append(a)
print(sum(memory))
