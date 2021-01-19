x = [25,75,44,55,63,23,11,2,44,99,6,38]

for i in range(len(x)):
    for j in range(0,len(x)-i-1):
        if x[j]>x[j+1]:
            x[j] += x[j+1]
            x[j+1] = x[j] - x[j+1]
            x[j] = x[j] - x[j+1]
print(x)