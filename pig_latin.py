def pig_latin(word):
    i = 0
    for a in word:
        if a in "aeiou":
            break
        i += 1

    if i == 0:
        piggy = word + "yay"
    else:
        piggy = word[i:] + word[:i] + "ay"

    if word[:1].isupper():
        piggy = piggy.title()

    print(piggy)
    # return piggy

while True:
    pig = input("Enter word to translate into pig latin: ")
    pig_latin(pig)

