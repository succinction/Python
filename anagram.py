def anagram(cba, abc):
    if sorted(cba) == sorted(abc):
        print("yes: anagram")
anagram('pni', "nip")