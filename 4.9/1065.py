
N = input()
if int(N) <= 99: print(N)
else:
    plus = 0
    jari = []
    if int(N)==1000 : N = '999'
    for i in range(3): 
        jari.append(int(N[i])) 
    N = int(N)
    if (jari[0]+(jari[0]%2))/2<=jari[1]-1 & jari[1]-1<=(jari[0]+(jari[0]%2))/2+4: 
        plus += (jari[1]-(jari[0]+(jari[0]%2))/2)
    elif jari[1] >= (jari[0]+(jari[0]%2))/2+5:
        plus = 5
    if jari[2] >= 2*jari[1]-jari[0] & 2*jari[1]-jari[0]>=0: plus += 1
    print(int(94 + 5*jari[0] + plus))
    
