# crud

phonebook = {'Howard':{'name': 'Joe Howard', 'number': '555-098-0987'},
            'Jones': {'name': 'Chris Jones', 'number': "555-543-4321"},
            'Sabbath': {'name': 'Black Sabbath', 'number': "555-543-4321"},
            'Zeppelin': {'name': 'Led Zeppelin', 'number': "555-543-2880"}}

def lst():
    for item in phonebook:
        print(item)

def lookup(name):
    print('')
    print(phonebook[name]['name'])
    print(phonebook[name]['number'])

def delete(name):
    del phonebook[name]
    print('{} deleted'.format(name))

def add_entry(name):
    print('Adding entry... ')
    n = input('Enter Name: ').title()
    m = input('Enter Number: ')
    newname =  n[n.find(" ")+1:].lower().capitalize()
    phonebook[newname] = {'name': n, 'number': m}
    print('Entry added for {} : '.format(newname))
    lookup(newname)

def edit(name):
    a = str(input('For {} what would you like to edit? \n(name / number / both) '.format(name)))

    if a == 'name' :
        b = input('{} : change to?: '.format(phonebook[name]['name'])).lower().title()
        newname =  b[b.find(" ")+1:].lower().capitalize()
        print(' newname =  b[b.find(" "):] ')
        print(newname)
        phonebook[newname] = {'name':  b, 'number': phonebook[name]['number'] }
        del phonebook[name]
        name = newname
        print('phonebook updated: \n\n{} \n{} \n{}\n'.format(name, phonebook[name]['name'], phonebook[name]['number']))
    elif a == 'number':
        c = input('{} What would you like to change it to?: '.format(phonebook[name]['number']))
        phonebook[name]['number'] = c
        print('phonebook updated: \n\n{} \n{} \n{}\n'.format(name, phonebook[name]['name'], phonebook[name]['number']))
    elif a == 'both' :
        d = input('{} : change to?: '.format(phonebook[name]['name']))
        e = input('{} : change to?: '.format(phonebook[name]['number']))
        newname =  d[d.find(" ")+1:].lower().capitalize()
        phonebook[newname] = {'name': d, 'number': e}
        del phonebook[name]
        name = newname
        print('phonebook updated: \n\n{} \n{} \n{}\n'.format(name, phonebook[name]['name'], phonebook[name]['number']))
    else:
        edit(name)

while True:
    print("### PHONEBOOK ###")
    a = str.strip(input("function? (ls,add,del,look,ed,q) : "))
    if a == 'q':
        quit()
    if a == 'ls':
        lst()
        continue
    b = str.strip(input ("Who? ")).lower().capitalize()
    if a == 'look':
        lookup(b)
    elif a == 'add':
        add_entry(b)
    elif a == 'del':
        delete(b)
    elif a == 'ed':
        edit(b)
    else:
        print("entry invalid try again ")
