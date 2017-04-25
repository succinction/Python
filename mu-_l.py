from operator import mul


def mutate_list(lst, num):
    return list(map(lambda x: mul(x, num), lst))

def m_l(lst, num):
    return [mul(x, num) for x in lst]

nl = [1, 2, 3, 4, 5]
lis_1 = ['bananas', 'apples', 'oranges']

print(mutate_list(nl, int(input("how many ? : "))))
print(m_l(nl, int(input("how many ? : "))))
print(m_l(lis_1, int(input("how many ? : "))))


#
# def double(list, arg):
#     new_list = []
#     for item in list:
#         for it in range(arg):
#             new_list.append(item)
#     return new_list
#
#
# lis_1 = ['bananas', 'apples', 'oranges']
# lis_2 = ['birds', 'dogs', 'cats']
#
# print( double(lis_2, int(input("how many ? : "))))