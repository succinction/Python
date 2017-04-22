
def fb(n):

    for i in range(int(n)):
        i += 1
        x = ''
        if i % 3 == 0:
            x = "Fizz"
        if i % 5 == 0:
            x += "Buzz"
        if x == '':
            print(i)
        else:
            print(x)

fb(input("How many times? : "))


print( (1==1) * 5 )