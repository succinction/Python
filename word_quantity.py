'''
Write a function that quanitifies word occourances in a given string.
'''

dictionary = {}

def quantify_words(text):
    txt = text.lower().split(' ')
    for v in txt:
        dictionary[v] = txt.count(v)

p = "Red touching black is a friend of Jack, Red touching yellow can kill a fellow."

quantify_words(p)
print(dictionary)
