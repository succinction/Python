
### 5 ############################################

# 5 Write a Python program to copy the contents of a file to another file.

filename = "hello_kitty.txt"


# filename = "hello.txt"
def copy_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    with open('hello_kitty_copy.txt', "w") as f:
        f.write(contents)
    with open('hello_kitty_copy.txt', "r") as f:
        red = f.read()
    print(red)

copy_file(filename)
