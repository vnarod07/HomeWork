import random
def inp():
    try:
        n = int(input())
        if n<=1 or n>=6 :
            raise ValueError
        return n    
    except ValueError:
        return inp()

def multi(array1, array2):
    zeroarray = [[0 for i in range(len(array2[0]))] for j in range(len(array1))]
    N = len(array1)
    for i in range(len(array1)):
        for j in range(len(array1[0])):
            for k in range(len(array1[0])):
                zeroarray[i][j] += array1[i][k] * array2[k][j]
    return zeroarray
            
        

def add(array1, array2):
    zeroarray = [[0 for i in range(len(array1))] for j in range(len(array1[0]))]
    for i in range(len(array1)):
        for j in range(len(array1[0])):
            zeroarray[i][j] = array1[i][j] + array2[i][j]
    return zeroarray 

def arrayprint(array):
    print('[', end=' ')
    for i in range(len(array)):
        for j in range(len(array1[0])):
            print(array[i][j], end=' ')
        if i == len(array)-1:
            print(']')
        else:
            print()

            
            
    
N = inp()
array1 = [[random.random()*(N*N*10) for i in range(N)] for j in range(N)]
array2 = [[random.random()*(N*N*10) for i in range(N)] for j in range(N)]
array3 = [[random.random()*(N*N*10) for i in range(N)] for j in range(N)]
multiarray = multi(array1, array2)
addarray = add(multiarray, array3)
arrayprint(addarray)






