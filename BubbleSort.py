x = [25,75,99,6,38]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i]+=x[j]
            x[j]=x[i]-x[j]
            x[i]=x[i]-x[j]


print(x)