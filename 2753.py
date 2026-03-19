res = int(input())
if (res%4==0 and res%100>0)or(res%400==0):
    print(1)
else:
    print(0)
