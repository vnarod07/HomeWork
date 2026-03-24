out = [] ; T = int(input()) ; A = [] ; B=[]
for i in range(T):
    a, b = input().split()
    out.append(int(a)+int(b))
    A.append(int(a))
    B.append(int(b))
for j in range(T):
    print(f'Case #{j+1}: {A[j]} + {B[j]} = {out[j]}')
