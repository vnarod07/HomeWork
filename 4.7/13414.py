#다음은 pypy3로 실행하여 맞은 것. 
K,L = input().split() ; K=int(K) ; L=int(L)
K = min(K,L)
dic = {} ; respon = []

for i in range(L):
    res = input()
    respon.append(res)
    dic[res] = dic.get(res,0)+1
for j in respon:
    if K == 0 : break
    if dic[j] == 1:
        print(j) ; K-=1
    else:
        dic[j] -= 1
