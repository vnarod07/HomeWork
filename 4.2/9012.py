N = int(input())
for i in range(N):
    res = input()
    open = 0;close = 0 ; yesno = 0
    for j in res:
        if open < close: open = 0.1
        if j == "(": open +=1
        else: close += 1
    if open == close: yesno = 'YES'
    else: yesno = 'NO'
    print(yesno)
    
    
