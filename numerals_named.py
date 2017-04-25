names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
pre = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
def named(numb):
    if numb < 21:
        return names[numb]
    else:
        return pre[int(str(numb)[0])] + names[int(str(numb)[1])]

print(named(int(input("what number? "))))


