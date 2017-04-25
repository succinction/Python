
def double(list, arg):
    new_list = []
    for item in list:
        for it in range(arg):
            new_list.append(item)
    return new_list


lis_1 = ['bananas', 'apples', 'oranges']
lis_2 = ['birds', 'dogs', 'cats']

print( double(lis_2, int(input("how many ? : "))))
