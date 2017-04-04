def palindrome (arg):
    rev = arg[::-1]
    print("".join(reversed(arg)))
    print(arg, rev)
    if arg == rev:
        print('Yes! {} is a palindrome.'.format(arg))
        return True

trying = False
while trying == False:
    word = input("Check word: ")
    if palindrome(word):
        contin = input('Quit?: (Y)').lower()
        if contin == 'y':
            trying = True
