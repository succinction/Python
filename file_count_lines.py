
### 3 ############################################

filename = "hello_kitty.txt"


def count_lines():
    with open(filename, "r") as txt:
        lines = txt.readlines()
    print(len(lines))

count_lines()
