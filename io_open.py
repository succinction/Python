# from io import open
filename = "hello.txt"
def greet(name):
    with open(filename, "a") as f:
        f.write("Greetings {}!\n".format(name))
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

greet(input("What is your name ? "))
