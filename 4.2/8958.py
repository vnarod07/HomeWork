C = int(input())
for i in range(C):
    output = 0
    ox = input()
    
    sequence=0
    for j in range(len(ox)):
        if ox[j] == 'O':
            if j == len(ox)-1: output += (0.5*(sequence+1)*(sequence+2))
            else: sequence+=1
        else:
            output += (0.5*sequence*(sequence+1))
            sequence=0
    print(int(output))

            
            
