
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