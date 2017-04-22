
x = 5
y  = ['the', 42, ['bye'] ]
lst = [x,x,x,y, 'another string']

print(lst)
print('Bye : ' + lst[3][2][0])
print('last thing : ' + lst[-1])

#######################
tuple = (x,x,x)
print(tuple[2])
dictionary = {'key1': 123, 'key2': 456}
print(dictionary['key1'])
#######################
print("################ rng = list(range(10))")

rng = list(range(10))
print(rng)

print("################")
lst2 = [23, 53, 3, 7, 19]
for v in lst2:
    v += 5
    print(v)

print("#######3#########")
lst3 = [23, 53, 3, 7, 19]
for i in range(len(lst3)):
    lst3[i] += 9
    print(i, lst3[i])
    print('\b\b\bindex: {}, value: {}'.format(i, lst3[i]))

print("#######4#########")
lsst = [3, 2,"hi"]

num = input('what is your fav num? : ')
lsst.append(int(num))
removed = lsst.pop(2)
print(lsst)
print(removed)
# print()
