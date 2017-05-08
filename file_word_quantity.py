
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

# quantify_words(filename)
quantify_words(input("File? : "))
print(dictionary)
print("#######################")

d = dictionary
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
for k, v in s:
    print(k, v)


