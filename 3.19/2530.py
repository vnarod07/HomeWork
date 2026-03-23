a,b,c = input().split()
a=int(a);b=int(b);c=int(c)
d = int(input())

if d >= 3600 * 24:
    d = d %(3600*24)

 
a += d // 3600
b += (d%3600)//60
c += (d%3600)%60


if c > 59 :
    c = c % 60
    b += 1
if b > 59 :
    b = b % 60
    a += 1
if a > 23:
    a = a % 24


print(f'{int(a)} {int(b)} {int(c)}')
