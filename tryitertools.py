import itertools

# counter = itertools.cycle([1,2,3])
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.count()
# data =[100,200,300,400]
# daily_data = list(itertools.zip_longest(data,range(10)))
#
# print(daily_data)


# def genex():
#     yield 1
#     yield 2
#     yield 3
#
#
# print(next(genex()))

# squares = map(pow,range(10),itertools.repeat(2))
#
# print(list(squares))

# squares = itertools.starmap(pow,[(1,2),(2,2),(3,2),(4,3)])
#
# #print(list(squares))
# for each in squares:
#     print(each)


num = [0,1,2,3]
letters = ['a','b','c','d']
names = ['utsav','subhash']

# res = itertools.combinations(letters,2)#combinations without value replacement
# for each in res:
#     print(each)

# res = itertools.permutations(letters,2)#permutations - with repeated values
# for each in res:
#     print(each)

# res = itertools.product(num,repeat=2)#combinations with value replacement
# for each in res:
#     print(each)

# res = itertools.combinations_with_replacement(num, 2) #combinations with value replacement
# for each in res:
#     print(each)

# combined = itertools.chain(letters,num,names)
#
# print(next(combined))

result= itertools.islice(range(10),1,5,2)
print(list(result))