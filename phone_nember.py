def phone(number):
    return "({}){}-{}".format(number[:3],number[3:6],number[6:])

print(phone(str(input("number? : "))))