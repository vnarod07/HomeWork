N, X = input().split();N=int(N);X=int(X)
res = input().split() ; output = []
for i in res:
    if int(i) < X:
        output.append(i)
for j in output:
    print(j, end=' ')    
