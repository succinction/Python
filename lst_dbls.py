def times_list(list1, n):
    new_list = []
    for i in list1:
        if i == 0:
            pass
        else:
            new_list.append(i * int(n))
    print(new_list)


list2 = [3, 5, 66, 7, 8, 12, 0, 45]
times_list(list2, 5)


def rocket(range, n):
    new_list = []
    for i in range:
        if i == 0:
            pass
        else:
            new_list.append(i * int(n))
    print(new_list)


list5 = [4, 0, 0, 0, 0, 5, 9, 0, 0, 0, 7, 8]
rocket(list5, 100)
