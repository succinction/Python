from io import open
filename = "hello.txt"
def greet(name):
    with open(filename, "w") as f:
        f.write("Greetings {}!".format(name))
    with open(filename, "r") as f:
        print(f.readline())

greet("John")
