N = int(input())
inp = list(map(int, input().split()))
max=-1000000 ; min=1000000
for i in inp:
    if i>=max: max=i
    elif i<=min: min=i
print(f'{min} {max}')
    
