N = int(input())
for i in range(N):
    if N % 2 == 0:
        print('* ' * (int(N/2)) + '\n' + ' *' * int((N/2)))
    else:
        print('* ' * (int((N+1)/2)) + '\n' + ' *' * int(((N-1)/2)) + ' ')
        
        
