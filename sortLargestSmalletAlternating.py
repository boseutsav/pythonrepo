from math import ceil

numarr = [int(x) for x in input('enter comma separated nums:').split(',')]

for each in numarr:
    print(each)

for i in range(len(numarr)):
    for j in range(i + 1, len(numarr)):
        if numarr[i] > numarr[j]:
            numarr[i] += numarr[j]
            numarr[j] = numarr[i] - numarr[j]
            numarr[i] = numarr[i] - numarr[j]
altarr =[]
for i in range(ceil(len(numarr)/2.0)):
    altarr.append(numarr[len(numarr)-i-1])
    if i<=(len(numarr)/2):
        altarr.append(numarr[i])
print(altarr)