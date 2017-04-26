
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