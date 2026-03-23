output = [] 

a,b,c,d = input().split()
e,f,g,h = input().split()
i,j,k,l = input().split()


def play(a,b,c,d):
    a=int(a);b=int(b);c=int(c);d=int(d)
    if a+b+c+d == 1:
        output.append('C')
    elif a+b+c+d == 2:
        output.append('B')
    elif a+b+c+d == 3:
        output.append('A')
    elif a+b+c+d == 4:
        output.append('E')
    else:
        output.append('D')

play(a,b,c,d)
play(e,f,g,h)
play(i,j,k,l)

for j in range(3):
    print(output[j])
