inp = []
for i in range(9):
    inp.append(int(input()))
    
max=0;posi=0
for i in range(9):
    if inp[i] >= max:
        max = inp[i]
        posi = i
print(max) ; print(posi+1)
