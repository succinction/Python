# dictionary = {}
#
# def quantify_words(input):
#     user_input = input(' ').split()
#     for occurence in user_input:
#         dictionary[occurence] = user_input.count(occurence)
#
# quantify_words(input)
# print(dictionary)

def front_back(str):
    if str == '':
        str = '12345'
    a = str[len(str)-1:len(str)]            # last
    b = str[1:-1]                           # middle
    c = str[0:1]                            # first
    v = a + b + c
    print(a)
    print(b)
    print(c)
    print(v)

front_back(input("what string? "))
