import random
def inp():
    try:
        n = int(input())
        if n<=1 or n>=6 :
            raise ValueError
        return n    
    except ValueError:
        return inp()

def arrayprint(array):
    print('[', end=' ')
    for i in range(len(array)):
        for j in range(len(array1[0])):
            print(array[i][j], end=' ')
        if i == len(array)-1:
            print(']')
        else:
            print()

def transposearray(array):
    zeroarray = [[0 for i in range(len(array[0]))] for j in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            zeroarray[i][j] = array[j][i]
    return zeroarray
    
            
            
    
N = inp()
array1 = [[random.random()*(N*N*10) for i in range(N)] for j in range(N)]
transarray = transposearray(array1)
arrayprint(transarray)




