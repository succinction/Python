my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 0):
    print(c, value)

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)