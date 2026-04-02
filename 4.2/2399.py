N = int(input()) ; sum=0
dots = list(map(int, input().split())) ; dots.sort()
for i in range(N): sum += dots[i] * (2*i-N+1)
print(sum*2)
