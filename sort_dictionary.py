d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
for k, v in s:
    print(k, v)

