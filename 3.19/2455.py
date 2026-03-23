max = 0 ; current = 0
for i in range(4):
    a, b = input().split()
    current += (int(b)-int(a))
    if current >= max:
        max = current
print(max)
    
