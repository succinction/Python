def greet(name):
    print('Hello {}'.format(name) )
a = greet
a('Joe')


def greeting(name, home='yes', age=30):
    # print('Hello {}, you are {}'.format(name, age))
     'Hello {}, you are {}'.format(name, age)
name = input("what's your name: ")
thing = greeting(name, age=35)
print(thing)
# OR
# print(greeting(name, age=35))
