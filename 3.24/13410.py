
max = 0
N, K = input().split() ; N=int(N) ; K=int(K)
for i in range(K, 0, -1 ):
    s = int(str(N*i)[::-1])
    if max <= s:
        max = s
print(max)
