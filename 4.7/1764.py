M, N = input().split()
M=int(M) ; N=int(N)
a = []
for i in range(M+N):
    a.append(input())

b = set(a[:N]) & set(a[N:])
b = sorted(b)

print(len(b))
for i in b:
    print(i)
