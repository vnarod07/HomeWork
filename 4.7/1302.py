N = int(input())
dic = {}

for i in range(N):
    a = input()
    dic.update({a : dic.get(a,0)+1})

lis = [i for i in dic.keys() if dic[i]==max(dic.values())]
lis.sort()
print(lis[0])
