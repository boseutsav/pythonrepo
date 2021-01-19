inputstr = input('Enter you statement:').split()
unq = []
for each in inputstr:
    if each not in unq:
        unq.append(each)

print(' '.join(unq))

