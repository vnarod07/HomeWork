N = int(input())
for i in range(2*N-1):
    if i >= N: print('*' * (2*N-i-1))
    else: print('*' * (i+1))
