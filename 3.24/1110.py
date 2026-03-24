N = input()
if len(N) == 2:
    ten = int(N[0]) ;  oriten = int(N[0])
    one = int(N[1]) ; orione = int(N[1])
else:
    ten = 0 ; oriten = 0
    one = int(N[0]) ; orione = int(N[0])
count = 0

while ((ten != oriten or (one != orione))) or count == 0:
    if ten+one>=10: n = str(ten+11*one-10) 
    elif ten==0: n = str(11*one)
    else: n = str(ten+11*one)
    if len(n) == 2:
      ten = int(n[0])
      one = int(n[1])
    else:
      ten = 0
      one = int(n[0])
    count += 1
print(count)
