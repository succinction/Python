
def to_snake (arg):
    # print(len(arg))
    indexes = []
    nextn = 0
    for n in range(len(arg)):
        if arg[n].isupper():
            indexes.append(arg[nextn:n].lower())
            nextn = n
    indexes.append(arg[nextn:len(arg)].lower())

    snake = "_".join(indexes)
    print(snake)
    return snake
to_snake('oneTwoThreeFour')

def toCamel (arg):
    lst = arg.split('_')
    newlst = []
    for i in range(len(lst)):
        ############################
        if i > 0:
            newlst.append(lst[i].capitalize())
        else:
            newlst.append(lst[i])
        ############################
    val = "".join(newlst)
    print(val)
    return val
toCamel("five_six_seven_eight")

def test_case (arg):
    snake_case = False
    if arg.find("_") != -1:
        snake_case = True
        print('')
        print('snake_case')
        print('CONVERT ' + arg + " to > ")
        toCamel(arg)
    else:
        for n in range(len(arg)):
            if arg[n].isupper():
                print('')
                print('camelCase')
                print('CONVERT ' + arg + ' to > ')
                to_snake(arg)
                return

done = False
while done == False:
    print("#######################")
    test_case(input('Test case: '))
    print("")
    print("#######################")
    if input("Keep playing? (y/n) ") == 'n':
        done = True
