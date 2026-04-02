rest = [] ; output = 0
for i in range(10):
    res = int(input())
    if res%42 in rest:
        pass
    else:
        rest.append(res%42)
        output += 1
print(output)
        
        
    
