import math
from itertools import count, islice

def is_prime(num):
    if num in [0, 1]:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    for each in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % each == 0:
            return False
    else:
        return True


#generator expression

res = sum(islice((x for x in count(start=1) if is_prime(x)),1000))

print(res)