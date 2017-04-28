number_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
pre_number = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def number_named(numb):
    if numb < 21:
        return number_names[numb]
    else:
        return pre[int(str(numb)[0])] + number_names[int(str(numb)[1])]

# print(named(int(input("what number? "))))


