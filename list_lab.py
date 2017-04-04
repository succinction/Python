#print(
# '''
# Create and empty list
# append 3 names to the names gathered from inputs
# use a for loop to greet each person.
# '''
# )

# import math
#from math import sqrt, pow
#
# lst = []
# name_dict = {}
# name_dict[0] = input('name 1 ? : ')
# name_dict[1] = input('name 2 ? : ')
# name_dict[2] = input('name 3 ? : ')
# #
# # WORKS
# print("########## LAB ###############")
# name = []
# name.append(input('name 1 ? : '))
# name.append(input('name 2 ? : '))
# name.append(input('name 3 ? : '))
# greetings = ["Welcome", "hello", "Hi"]
# for v in range(len(name)):
#     print ("{} {}".format(greetings[v], name[v]) )
# #########################
# print("########## EXTRA LAB ###############")
# person = []
# person.append(input('what is your name ? : '))
# person.append(int(input('what is your age ? : ')))
# person[1] += 1
# print("Welcome {}. Next year you will be {}".format(person[0], int(person[1])+1 ))
# ########################
print("########## EXTRA LAB 2 ###############")
# INSERT
# pop
# EXTEND
store = []
store2 = []
fruit = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
meat = ['beef', 'chicken', 'pork']
starch = ['tortillas', 'bread']
store.extend(fruit)
store.extend(meat)
store.extend(starch)
#
store2.append(fruit)
store2.append(meat)
store2.append(starch)
print(store,'\n OR \n', store2)
# for value in store:
#     print('from store> ' + value)
# for value in store2:
#     print('from store2 : ' + str(value))
print("####################################")
import random
for v in range(len(store)):
    va = store.pop(  random.randrange( len(store) ) )
    print('random : ' + va)

print('remains: ', store)

#############################  FURTHER
