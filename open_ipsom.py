""" 
For this lab we are going to pick 3 of the following:

1 Write a Python program to read first n lines of a text file.
2 Write a python program to find the longest words in a text file.
3 Write a Python program to count the number of lines in a text file
4 Write a Python program to count the frequency of words in a file.
5 Write a Python program to copy the contents of a file to another file.

Each should be written in it's own file.
"""
## 1 #############################################

filename = "hello_kitty.txt"

def read_first(num):
    with open(filename, "r") as txt:
        lines = txt.readlines()
        print(lines[:num])

read_first(3)

### 2 ############################################

filename = "hello_kitty.txt"

def choose_longer(args):
    string = ''
    for x in args:
        if len(x) > len(string):
            print("'{}' > '{}'".format(x, string))
            print("'{}' > '{}'".format(len(x), len(string)))
            string = x
    print(string, "<<<")

def longest_words():
    with open(filename, "r") as txt:
        lines = txt.readlines()
        words = [word for line in lines for word in line.split(" ")]
        # .strip()
    choose_longer(words)

longest_words()

### 3 ############################################

filename = "hello_kitty.txt"


def count_lines():
    with open(filename, "r") as txt:
        lines = txt.readlines()
    print(len(lines))

count_lines()

### 4 ############################################

filename = "hello_kitty.txt"

dictionary = {}
def quantify_words(filename):
    with open(filename, "r") as txt:
        lines = txt.readlines()
        words = [word for line in lines for word in line.split(" ")]

    # txt = words.split(' ')
    for v in words:
        dictionary[v] = words.count(v)

# p = "Red touching black is a friend of Jack, Red touching yellow can kill a fellow."

quantify_words(filename)
print(dictionary)


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


