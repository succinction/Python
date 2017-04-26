
## 1 #############################################

filename = "hello_kitty.txt"

def read_first(num):
    with open(filename, "r") as txt:
        lines = txt.readlines()
        print(lines[:num])

read_first(3)

